// Read-only browser preflight for Code Video. Not final MP4 or aesthetic approval.
import fs from 'node:fs';
import http from 'node:http';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {createRequire} from 'node:module';
import {spawnSync} from 'node:child_process';
import {fileURLToPath, pathToFileURL} from 'node:url';
import {parseArgs} from 'node:util';

const {values: args} = parseArgs({options: {
  project: {type:'string'}, duration:{type:'string'}, reference:{type:'string'},
  width:{type:'string', default:'1920'}, height:{type:'string', default:'1080'},
  fps:{type:'string', default:'30'}, 'playwright-module':{type:'string'},
  ffmpeg:{type:'string', default:'ffmpeg'}, 'allow-helper-changes':{type:'boolean', default:false},
  'offline-only':{type:'boolean', default:false}, help:{type:'boolean', default:false},
}});
if (args.help) {
  console.log('node preflight.mjs --project ABS_DIR --duration SECONDS [--reference CODE_VIDEO_ROOT] [--width 1920 --height 1080 --fps 30] [--playwright-module ABS_MODULE] [--ffmpeg ABS_EXECUTABLE] [--offline-only]');
  process.exit(0);
}
const skill = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const sha = file => createHash('sha256').update(fs.readFileSync(file)).digest('hex');
let browser, server;
try {
  if (!args.project || !path.isAbsolute(args.project)) throw Error('--project must be an absolute directory.');
  const root = fs.realpathSync(args.project);
  const reference = fs.realpathSync(args.reference ?? path.join(skill, '../code-video'));
  const expected = {w:Number(args.width), h:Number(args.height), fps:Number(args.fps), dur:Number(args.duration)};
  if (![expected.w, expected.h, expected.fps, expected.dur].every(n => Number.isFinite(n) && n > 0)
      || !Number.isInteger(expected.w) || !Number.isInteger(expected.h)) throw Error('Supply positive duration/specification.');
  if (Math.abs(expected.fps * expected.dur - Math.round(expected.fps * expected.dur)) > 1e-6)
    throw Error('Expected duration * fps must be an integer frame count.');
  for (const name of ['index.html','main.js','kit.js','render.mjs']) {
    if (!fs.statSync(path.join(root,name)).isFile()) throw Error('Missing project file: '+name);
  }
  const helpers = {};
  for (const name of ['kit.js','render.mjs']) {
    const actual = sha(path.join(root,name)), baseline = sha(path.join(reference,'template',name));
    helpers[name] = {sha256:actual, referenceSha256:baseline, unchanged:actual===baseline};
    if (actual !== baseline && !args['allow-helper-changes']) throw Error('Changed upstream helper: '+name+'. Inspect diff/authorization; do not bypass silently.');
  }
  const version = spawnSync(args.ffmpeg,['-version'],{encoding:'utf8'});
  if (version.error || version.status !== 0) throw Error('FFmpeg executable unavailable: '+args.ffmpeg);
  const encoders = spawnSync(args.ffmpeg,['-hide_banner','-encoders'],{encoding:'utf8'});
  if (encoders.status !== 0 || !/\blibx264\b/.test(encoders.stdout ?? '')) throw Error('FFmpeg lacks libx264.');
  let modulePath = args['playwright-module'];
  if (!modulePath) {
    try { modulePath = createRequire(path.join(root,'package.json')).resolve('playwright-core'); }
    catch { throw Error('Install project playwright-core or provide --playwright-module ABS_MODULE.'); }
  }
  const imported = await import(pathToFileURL(path.resolve(modulePath)).href);
  const chromium = imported.chromium ?? imported.default?.chromium;
  if (!chromium) throw Error('Module does not export chromium.');
  const mime = {'.html':'text/html; charset=utf-8','.js':'text/javascript','.mjs':'text/javascript',
    '.json':'application/json','.ttf':'font/ttf','.otf':'font/otf','.woff':'font/woff','.woff2':'font/woff2',
    '.png':'image/png','.jpg':'image/jpeg','.wav':'audio/wav'};
  server = http.createServer((req,res) => {
    try {
      let requested = decodeURIComponent(new URL(req.url,'http://localhost').pathname);
      if (requested === '/') requested = '/index.html';
      const candidate = path.resolve(root,'.'+requested);
      if (!candidate.startsWith(root+path.sep)) return res.writeHead(403).end();
      let target;
      try { target = fs.realpathSync(candidate); } catch { return res.writeHead(404).end(); }
      if (!target.startsWith(root+path.sep)) return res.writeHead(403).end();
      fs.readFile(target,(err,bytes) => err ? res.writeHead(404).end() :
        res.writeHead(200,{'content-type':mime[path.extname(target)] ?? 'application/octet-stream'}).end(bytes));
    } catch { res.writeHead(400).end(); }
  });
  await new Promise((resolve,reject) => {server.once('error',reject);server.listen(0,'127.0.0.1',resolve);});
  const errors = [], failedAssets = [], external = new Set();
  browser = await chromium.launch({channel:'chrome',headless:true});
  const page = await browser.newPage({viewport:{width:expected.w,height:expected.h}});
  page.on('pageerror',e => errors.push(e.message));
  page.on('request',req => { const u = new URL(req.url()); if (['http:','https:'].includes(u.protocol) && u.hostname !== '127.0.0.1') external.add(req.url()); });
  page.on('requestfailed',req => failedAssets.push(req.url()));
  page.on('response',res => {if (res.status() >= 400 && !res.url().endsWith('/favicon.ico')) failedAssets.push(res.url());});
  await page.goto(`http://127.0.0.1:${server.address().port}/index.html`,{waitUntil:'load'});
  await page.waitForFunction(() => window.READY === true,null,{timeout:30000});
  await page.evaluate(() => document.fonts.ready);
  const meta = await page.evaluate(() => ({video:window.VIDEO,
    fonts:[...document.fonts].map(f => ({family:f.family,weight:f.weight,status:f.status})),
    canvas:{width:document.querySelector('#c')?.width,height:document.querySelector('#c')?.height},
    renderFrame:typeof window.renderFrame}));
  if (!meta.video || meta.renderFrame !== 'function') throw Error('Missing VIDEO/renderFrame runtime contract.');
  for (const [key,value] of Object.entries(expected)) {
    if (typeof meta.video[key] !== 'number' || Math.abs(meta.video[key]-value) > 1e-6)
      throw Error(`Wrong loaded timeline ${key}: actual=${meta.video[key]}, expected=${value}; directory=${root}`);
  }
  if (meta.canvas.width !== expected.w || meta.canvas.height !== expected.h) throw Error('Canvas physical size differs from VIDEO.');
  const unloaded = meta.fonts.filter(f => f.status !== 'loaded');
  if (unloaded.length) throw Error('Fonts not loaded: '+JSON.stringify(unloaded));
  const total = Math.round(expected.fps*expected.dur);
  const checkedFrames = [...new Set([0,Math.floor(total/2),total-1])];
  for (const frame of checkedFrames) await page.evaluate(async f => {await window.renderFrame(f);},frame);
  if (errors.length) throw Error('Browser runtime errors: '+errors.join('; '));
  if (failedAssets.length) throw Error('Asset load failures: '+[...new Set(failedAssets)].join('; '));
  if (args['offline-only'] && external.size) throw Error('External resources in offline-only project: '+[...external].join('; '));
  console.log(JSON.stringify({pass:true,projectDirectory:root,expectedFrames:total,
    ...meta,helpers,mainSha256:sha(path.join(root,'main.js')),checkedSourceFrames:checkedFrames,
    externalResources:[...external],ffmpegVersion:version.stdout.split('\n')[0],
    warnings:['Font loaded status does not establish correct glyphs/Chinese coverage.',
              'Source frame execution is not visual inspection or encoded MP4 verification.'],
    scope:'Read-only runtime preflight. No render approval, aesthetic pass, final video check, or delivery claim.'},null,2));
} catch (error) {
  console.error(JSON.stringify({pass:false,error:error.message,scope:'Preflight only.'},null,2));
  process.exitCode = 1;
} finally {
  if (browser) await browser.close();
  if (server?.listening) await new Promise(resolve => server.close(resolve));
}
