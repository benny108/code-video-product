#!/usr/bin/env python3
"""Select the actual Code Video style guide and its production risks; no rendering."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

SKILL = Path(__file__).resolve().parents[1]
CATALOG = SKILL / 'references/style-catalog.json'


def sections(text):
    result = {}
    current = '_intro'
    lines = []
    for line in text.splitlines():
        if line.startswith('## '):
            result[current] = '\n'.join(lines).strip()
            current = line[3:].strip()
            lines = []
        else:
            lines.append(line)
    result[current] = '\n'.join(lines).strip()
    return result


def normalize(value):
    value = value.strip()
    if '://' in value:
        fragment = urlparse(value).fragment
        if not fragment:
            raise ValueError('画廊链接缺少风格锚点；请指定 slug 或名称。')
        value = fragment
    value = unquote(value.lstrip('#')).strip().lower()
    if value.isdigit():
        value = str(int(value)).zfill(2)
    return value


def resolve_style(value, catalog, root):
    key = normalize(value)
    matches = []
    for item in catalog['styles']:
        names = [item['slug'], item['name'], item['number']] + item['aliases']
        if key in [normalize(n) for n in names]:
            matches.append(item)
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        raise ValueError('画风名称不唯一，请使用明确 slug。')
    # Future upstream styles can be used without rewriting this catalog.
    if re.fullmatch(r'[a-z][a-z0-9-]*', key):
        candidate = root / 'references/styles' / (key + '.md')
        if candidate.is_file():
            return {'number': None, 'slug': key, 'name': key, 'guide': candidate.name,
                    'preset': None, 'aliases': [], 'guide_sha256_at_creation': None}
    raise ValueError('无法确定画风：%s；用 --list 查看，或给出存在的指南 slug。' % value)


def brand_core(guide, preset):
    s = sections(guide)
    chunks = []
    if preset:
        rows = [line for line in s.get('Presets', '').splitlines()
                if line.startswith('| `'+preset+'` |')]
        if not rows:
            raise ValueError('当前指南不包含所选品牌 preset：'+preset)
        chunks += ['## 所选 preset：'+preset,
                   '| Preset | Stages | Type | Signature moves | Pacing |',
                   '|---|---|---|---|---|', rows[0]]
        table = [line for line in s.get('Preset tokens', '').splitlines()
                 if line.startswith('|')]
        header = [cell.strip() for cell in table[0].strip('|').split('|')]
        index = header.index(preset)
        chunks += ['\n## 所选 token', '| Token | Value |', '|---|---|']
        for row in table[2:]:
            cells = [c.strip() for c in row.strip('|').split('|')]
            if len(cells) > index:
                chunks.append('| '+cells[0]+' | '+cells[index]+' |')
    else:
        # DESIGN.md-driven mode: do not invent Stripe tokens from another preset.
        for heading in ['Pick the source of the tokens', 'Map a DESIGN.md to tokens']:
            if heading in s:
                chunks += ['## '+heading, s[heading]]
        chunks += ['\n此项需要对应 DESIGN.md/真实参考的 token，不是额外内置 preset。']
    chunks += ['\n## Signature', s.get('Signature', '')]
    return '\n'.join(chunks)


def make_packet(value, root, mode):
    catalog = json.loads(CATALOG.read_text(encoding='utf-8'))
    item = resolve_style(value, catalog, root)
    guide_path = root / 'references/styles' / item['guide']
    if not guide_path.is_file():
        raise ValueError('指南缺失：%s；用 --code-video-root 指定真实安装/参考目录。' % guide_path)
    raw = guide_path.read_bytes()
    text = raw.decode('utf-8')
    digest = hashlib.sha256(raw).hexdigest()
    production_path = SKILL/'references'/item.get('production_guide', 'styles/'+item['slug']+'.md')
    production_text = None
    production_sha = None
    if production_path.is_file():
        production_bytes = production_path.read_bytes()
        production_text = production_bytes.decode('utf-8')
        production_sha = hashlib.sha256(production_bytes).hexdigest()
    elif item.get('production_guide'):
        raise ValueError('索引中的中文制作指南缺失：'+str(production_path))
    warnings = []
    old = item['guide_sha256_at_creation']
    if old and old != digest:
        warnings.append('当前指南与索引建立时版本不同；以当前指南和实际参考为准，重新确认差异。')
    paths = [root/'docs/gallery'/(item['slug']+'.gif'),
             root/'docs/styles'/(item['slug']+'.jpg')]
    local_media = [str(p.resolve()) for p in paths if p.is_file()]
    if not local_media:
        warnings.append('未找到该风格的本地 GIF/高清图；本包只有文本依据，不能声称已观察原动作。')
    risk = sections((SKILL/'references/style-risk-map.md').read_text(encoding='utf-8'))
    risk_key = 'brand' if item['guide'] == 'brand.md' else item['slug']
    if item['guide'] == 'brand.md':
        core = brand_core(text, item['preset'])
    else:
        s = sections(text)
        headings = ['Inputs to ask for', 'Signature', 'Look', 'Rules', 'Direction']
        chunks = [s['_intro']]
        chunks += ['## '+h+'\n'+s[h] for h in headings if h in s]
        # Include any additional guide constraints; do not silently drop them.
        chunks += ['## '+h+'\n'+body for h, body in s.items()
                   if h != '_intro' and h not in headings]
        core = '\n\n'.join(chunks)
    return {'style': item['slug'], 'name': item['name'], 'gallery_number': item['number'],
            'features': item.get('features'),
            'suitable_scenarios': item.get('suitable_scenarios', []),
            'example_topic': item.get('example_topic'),
            'selection_boundary': item.get('selection_boundary'),
            'mode': mode, 'guide_path': str(guide_path.resolve()), 'guide_sha256': digest,
            'upstream_repository': catalog['upstream_repository'],
            'catalog_guide_url': item.get('guide_url'),
            'catalog_preview_url': item.get('preview_url'),
            'production_guide_path': str(production_path.resolve()) if production_text else None,
            'production_guide_sha256': production_sha,
            'production_guide': production_text,
            'catalog_reference_commit': catalog['observed_reference_commit'],
            'current_reference_commit_verified': False,
            'local_reference_media': local_media,
            'official_full_video_verified': False, 'warnings': warnings,
            'core_from_actual_guide': core, 'related_production_risks': risk.get(risk_key, ''),
            'scope': '仅定位参考/提取文本。未查看媒体、未测构图比例、未渲染、未验收。'}


def markdown(packet):
    modes = {'reproduction': '完整原例复现', 'new-content': '同画风新内容',
             'adapted': '明确授权改编', 'unspecified': '需从用户最新请求确定，不替用户改写目标'}
    lines = ['# '+packet['name']+' / '+packet['style'],
             '- GitHub 原项目：[Changroro/code-video]('+packet['upstream_repository']+')',
             '- 本次模式：'+modes[packet['mode']],
             '- 实际指南：'+packet['guide_path'],
             '- 指南 SHA256：'+packet['guide_sha256'],
             '- 索引历史参考 commit（非当前版本认证）：'+packet['catalog_reference_commit'],
             '- 当前是否存在官方完整片：未核验，不能根据本包推断。',
             '- '+packet['scope']]
    if packet['catalog_guide_url']:
        lines += ['- 固定历史参考：[GitHub 原指南]('+packet['catalog_guide_url']+')']
    if packet['catalog_preview_url']:
        lines += ['- 固定历史参考：[GitHub 原动图]('+packet['catalog_preview_url']+')']
    lines += ['- 本地参考：'+p for p in packet['local_reference_media']]
    lines += ['- 注意：'+w for w in packet['warnings']]
    if packet['production_guide']:
        lines += ['- 本画风中文制作指南：'+packet['production_guide_path'],
                  '- 中文制作指南 SHA256：'+packet['production_guide_sha256'],
                  '\n## 本画风中文制作指南\n', packet['production_guide']]
    else:
        lines += ['- 此项尚无本地中文制作指南；读取原指南后明确记录本次风格要求，不套其他画风。']
    lines += ['\n## 原指南的核心要点\n', packet['core_from_actual_guide']]
    if packet['related_production_risks']:
        lines += ['\n## 本画风的实际踩坑\n', packet['related_production_risks']]
    lines += ['\n## 接下来写入 STYLE-SPEC.md',
              '查看实际媒体后测量比例/构图，记录材质与字体、接触锚点、运动/转场/声音，',
              '区分不变量与用户可替换项；标明未知片段、风险时间窗和通过条件。',
              '参考流程：'+str(SKILL/'references/style-analysis.md')]
    return '\n'.join(lines)+'\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('style', nargs='?')
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--code-video-root', type=Path, default=SKILL.parent/'code-video')
    parser.add_argument('--mode', choices=['unspecified','reproduction','new-content','adapted'],
                        default='unspecified')
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--output', type=Path, help='Explicit new file; refuses to overwrite')
    args = parser.parse_args()
    try:
        catalog = json.loads(CATALOG.read_text(encoding='utf-8'))
        if args.list:
            if args.style:
                raise ValueError('--list 不同时接受单个画风。')
            rendered = ('\n'.join('%s  %-18s %s' % (i['number'], i['slug'], i['name'])
                                  for i in catalog['styles'])+'\n')
        else:
            if not args.style:
                parser.error('需要画风名称/编号/锚点，或 --list。')
            p = make_packet(args.style, args.code_video_root.expanduser().resolve(), args.mode)
            rendered = json.dumps(p, ensure_ascii=False, indent=2)+'\n' if args.json else markdown(p)
        if args.output:
            with args.output.expanduser().open('x', encoding='utf-8') as file:
                file.write(rendered)
            print('已写入：'+str(args.output.expanduser().resolve()))
        else:
            print(rendered, end='')
    except (OSError, ValueError) as error:
        print('ERROR: '+str(error), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
