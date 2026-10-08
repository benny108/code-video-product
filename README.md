# Code Video Product

**按参考画风做程序动画，而不是换个背景、放个通用人物，就声称还原了模板。**

一个面向 Codex 的中文 Skill：为 [Changroro/code-video](https://github.com/Changroro/code-video) 补充 **38 种画风的选型、制作要求、实际踩坑和分层验收**，支持原例复现、同画风新内容和明确授权的改编。

> 本仓库是独立的生产与验收扩展，不是 Code Video 官方发行版，不包含 38 套完整场景源码、原作者完整视频或一键出片服务。

**快速入口：** [38 种画风：特点与适用场景](references/style-catalog.md) · [Skill 指令](SKILL.md) · [制作踩坑](references/production-pitfalls.md) · [验收标准](references/acceptance.md)

## 能帮你解决什么

| 常见问题 | 这里怎么处理 |
|---|---|
| 不知道该用哪个画风 | 按编号、中文名、slug 或画廊链接定位；每种有特点、适用场景、选题示例和边界。 |
| 成片与参考只有颜色相似 | 分别提取人物比例、道具关系、材质、字体、镜头、动作与转场，不跨画风套同一个通用人物。 |
| 动了，但像演示文稿 | 按接触、受力、揭晓、反馈等语义事件安排动作，不规定所有视频相同的五段式或触发秒点。 |
| 一次整片渲染后才发现大问题 | 先查原尺寸构图和核心风险动作段，再做整片；退修按具体时间与缺陷定位。 |
| 在错误目录渲染了旧时间线 | 预检实际 HTML 的时长、规格、运行时与上游 helper SHA。 |
| 脚本退出成功就算交付 | 区分技术、画面、声音、工程可移植性和真实播放验收；最终检查实际编码 MP4。 |
| 配音有念稿感、音效机械重复 | 按意群、转折与理解停留处理节奏；声音跟事件走，服从本次声音偏好。 |

这个 Skill 不会自动替你发布视频、上传声音样本、生成额外集数，或把短 GIF 循环当成完整原例。

## 安装

### 1. 与 Code Video 相邻安装

以下命令适用于**尚未安装这两个仓库**的环境。已有目录请保留，按下一节指定路径，不要为了安装覆盖现有工程。

```bash
SKILLS_ROOT="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$SKILLS_ROOT"

git clone https://github.com/Changroro/code-video.git "$SKILLS_ROOT/code-video"
git -C "$SKILLS_ROOT/code-video" checkout --detach 03da4e3ab149c4134a9a72eec499e1a2a41601ea

git clone https://github.com/benny108/code-video-product.git "$SKILLS_ROOT/code-video-product"
```

重新加载 Skill 列表后，可在 Codex 中使用 `$code-video-product`。其他支持 `SKILL.md` 的工具也可读取该文件；工具自身的安装方式和能力可能不同。

上游固定在 `03da4e3ab149c4134a9a72eec499e1a2a41601ea`，方便对照和复现，**不是宣称这是上游最新版本**。使用其他版本时，脚本会提示已记录的指南 SHA 差异，需要重新核对媒体和约束。

### 2. 已有上游安装，或只想看文档

- 仅阅读中文指南、查看目录和运行 `--list`：不需要下载原视频、安装 Node 或配置 TTS。
- 提取风格工作包：需要 Python 3 和实际上游指南；Python 脚本只使用标准库。
- 上游位于其他目录：通过 `--code-video-root /absolute/code-video` 指定，不需要复制到固定私人路径。
- 没有 `~/.codex/tts-preferences.json` 也能使用；它只是可选的本地声音偏好，不随本仓库提供。

### 3. 做视频时的额外依赖

| 阶段 | 依赖 |
|---|---|
| 风格选择、中文工作包、单元测试 | Python 3；实际上游 `references/styles`，测试还会检查本地预览媒体。 |
| `preflight.mjs` 浏览器预检 | Node.js 20+、Google Chrome、`playwright-core`、带 `libx264` 的 FFmpeg、上游 `template` 和已有视频工程。 |
| 完整渲染、音效、节拍辅助 | 按所用上游版本的 [README](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/README.md) 安装；部分上游辅助脚本需要 `uv` 及音频处理依赖。 |

预检使用 `channel: 'chrome'`，**仅安装 Playwright 自带 Chromium 不够**。`playwright-core` 可以装在视频工程内，或用 `--playwright-module` 指向已有模块；不要将 `node_modules` 提交到本仓库。

## 在 Codex 中使用

先讲清楚要做哪种任务。以下是提示词示例，不是新任务或固定镜头数量。

### 同画风新内容

```text
使用 $code-video-product。
用 01 手绘小剧场讲“一个剪辑师为什么卖不出宣传片”。
横屏 1920×1080、30fps，约60秒。
先看原指南和原动图，保留纸面、细墨线、迷你角色比例与动作语言。
用人物和道具的互动解释客户需求，不要静态卡片加字幕。
先交核心动作短段与参考对照，通过后再渲染整片。
```

### 原例复现

```text
使用 $code-video-product，复现 02 侦探证据板原示例。
保持原主题、构图、人物与道具比例、材质、镜头、动作和声音方向。
只将我指定的几处文字中文化，不创作新品牌或新故事。
没有完整原片覆盖的部分，明确注明依据 GIF 与指南重建。
```

### 修订已有成片

```text
使用 $code-video-product，检查这份 RPG 工程和成片。
对照原参考，重点检查人物占比、像素细节、手与剑接触、敌人受力和经验更新顺序。
先给出具体时间点、缺陷和最小修法，再修改受影响段。
不要只用缩小通用方块人物来声称还原了 RPG 美术。
```

## 脚本用法

以下命令在本仓库根目录运行。这里的 `/absolute/...` 是需要替换的示例路径。

### 查画风、生成工作包

```bash
python3 scripts/style_brief.py --list
python3 scripts/style_brief.py 手绘
python3 scripts/style_brief.py 02 --mode reproduction
python3 scripts/style_brief.py '#detective' --mode new-content

python3 scripts/style_brief.py rpg \
  --code-video-root /absolute/code-video \
  --mode new-content \
  --json

python3 scripts/style_brief.py detective \
  --mode reproduction \
  --output /absolute/new-style-brief.md
```

支持带风格锚点的画廊 URL；“漫画”这种不明确的名称会报错，不擅自选 `comic` 或 `comicbook`。

工作包包含特点、适用场景、中文指南、实际上游指南要点、文件 SHA 和相关风险。`--output` 拒绝覆盖已有文件。**生成文本包不等于已经查看媒体、测量比例或通过画面验收。**

### 检查已有视频工程

```bash
node scripts/preflight.mjs \
  --project /absolute/video-project \
  --duration 60 \
  --reference /absolute/code-video \
  --width 1920 --height 1080 --fps 30
```

视频工程应有 `index.html`、`main.js`、`kit.js`、`render.mjs`，并暴露上游的 `READY`、`VIDEO`、`renderFrame` 运行时契约。

可选参数：

```bash
# 模块或 FFmpeg 不在默认查找位置时，添加对应参数
--playwright-module /absolute/node_modules/playwright-core/index.mjs
--ffmpeg /absolute/ffmpeg

# 要求没有外部 HTTP/HTTPS 资源时
--offline-only
```

预检输出 JSON，检查真实加载的规格与时长、字体加载、首/中/末源码帧运行、素材错误及 helper SHA。不改工程，也不编码视频。

**预检通过不代表美术达标**：它不确认中文真实字形、角色比例、音画因果、最终 MP4 或授权。`--allow-helper-changes` 仅用于已明确记录且获准的引擎改动，不能作为隐藏问题的默认开关。

## 38 种画风速览

详细的 **特点、适用场景、具体选题、选型边界、GitHub 原指南和原 GIF** 都在 [画风总目录](references/style-catalog.md)。编号沿用本地整理的 38 项画廊，不是上游通用编号。

| 内容语言 | 对应画风 |
|---|---|
| 故事、人物与教学 | [01 手绘小剧场](references/styles/handdrawn.md) · [03 像素RPG](references/styles/rpg.md) · [04 白板](references/styles/whiteboard.md) · [05 英雄漫画](references/styles/comic.md) · [11 街机](references/styles/arcade.md) · [13 翻页漫画](references/styles/comicbook.md) · [15 绘本](references/styles/storybook.md) |
| 调查、推理与记录 | [02 侦探证据板](references/styles/detective.md) · [14 博物馆](references/styles/museum.md) · [21 新闻](references/styles/news.md) · [22 剪贴簿](references/styles/scrapbook.md) · [31 数学推导](references/styles/mathlecture.md) · [32 纪录片](references/styles/documentary.md) |
| 结构、流程与界面 | [07 界面变形](references/styles/uimorph.md) · [08 热敏小票](references/styles/thermal.md) · [10 工程蓝图](references/styles/blueprint.md) · [12 装配说明书](references/styles/manual.md) · [18 机械翻牌](references/styles/splitflap.md) · [28 CRT终端](references/styles/terminal.md) · [33 地铁路线](references/styles/transit.md) |
| 产品与品牌展示 | [06 简洁动效](references/styles/motion.md) · [19 科技发布会](references/styles/brand-samsung.md) · [20 设计文档驱动](references/styles/designmd-stripe.md) · [26 暗色媒体](references/styles/brand-spotify.md) · [29 竞速奢华](references/styles/brand-ferrari.md) · [30 运动力量](references/styles/brand-nike.md) · [37 极简展台](references/styles/brand-apple.md) |
| 氛围、材质与揭晓 | [09 电影预告](references/styles/trailer.md) · [17 粒子](references/styles/particles.md) · [23 撕纸拼贴](references/styles/collage.md) · [24 沙画](references/styles/sand.md) · [25 霓虹](references/styles/neon.md) |
| 对比、节奏与自定设计 | [16 体育转播](references/styles/sports.md) · [27 电视购物](references/styles/infomercial.md) · [34 天气](references/styles/weather.md) · [35 动态歌词](references/styles/lyric.md) · [36 节拍同步](references/styles/beat.md) · [38 自由模式](references/styles/free.md) |

这些是选型分组，不是必须遵循的分类。几个重要区别：

- 手绘是**人物做事**；白板是**书写推动推理**。
- 英雄漫画强调**动作冲突**；翻页漫画强调**实体书和章节阅读**。
- RPG强调**角色、装备和成长**；街机强调**选关与短挑战**。
- 剪贴簿用照片记录经历；撕纸拼贴用纸片本身组成景物。
- 品牌名指设计语言，不表示品牌授权、合作或代言。
- `designmd-stripe` 依据真实 `DESIGN.md`，不是第六个固定品牌预设；`free` 也不是随意混搭或降低质量。
- 动态歌词是解释图加屏幕歌词，不自动生成演唱；节拍同步需要真实音轨和可使用的素材。

## 制作与验收路线

```text
确认模式与范围
   ↓
定位指南 + 查看实际参考
   ↓
记录 STYLE-SPEC：比例、材质、动作、镜头、声音和未知部分
   ↓
原尺寸构图 + 核心风险动作短段
   ↓
预检工程 → 渲染整片 → 检查实际编码 MP4
   ↓
独立工程包验证 + 来源许可 + 指定目标的真实播放检查
```

这是质量检查路线，不是强制每集相同的剧情结构。动作检查要看完整因果，例如“接触 → 受力 → 结算”，不是只抽几张好看的静帧。

进一步阅读：[风格分析与分镜](references/style-analysis.md) · [分层验收](references/acceptance.md) · [生产踩坑](references/production-pitfalls.md) · [各画风风险](references/style-risk-map.md)

## 仓库结构

```text
code-video-product/
├── README.md
├── SKILL.md                   # Codex 按需加载的制作指令
├── THIRD_PARTY_NOTICES.md      # 上游来源与许可说明
├── agents/openai.yaml         # Skill 界面元信息
├── references/
│   ├── style-catalog.md       # 38种画风特点、场景与指南入口
│   ├── style-catalog.json     # 机器可读索引
│   ├── styles/                # 38份独立中文制作指南
│   ├── style-analysis.md
│   ├── style-risk-map.md
│   ├── production-pitfalls.md
│   └── acceptance.md
└── scripts/
    ├── style_brief.py         # 定位与工作包，不渲染
    ├── preflight.mjs          # 只读运行时预检
    └── test_style_brief.py
```

不包含原视频、私人参考音、字体包、凭据、渲染工程或 `node_modules`。上游媒体与工具从原项目按需获取。

## 测试

已相邻安装上游时：

```bash
python3 -B scripts/test_style_brief.py
node --check scripts/preflight.mjs
```

上游在其他目录时：

```bash
CODE_VIDEO_ROOT=/absolute/code-video python3 -B scripts/test_style_brief.py
```

测试覆盖 38 项真实指南与中文指南、别名与 URL、品牌预设隔离、选型信息传递、版本变化、新画风降级处理，以及拒绝覆盖已有输出。这些测试不证明最终视频的美术或声音质量。

## 来源与许可

- 上游项目：[Changroro/code-video](https://github.com/Changroro/code-video)，固定参考 commit 见安装命令。
- 上游采用 MIT；完整声明保留在 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。本仓库不重新分发上游视频、字体或完整渲染引擎。
- 中文指南是依据原指南、可观察参考和制作退修经验整理的独立说明，不是官方译文。用途建议不代表官方原例剧情。
- 本仓库新增内容尚未另行指定开源许可证；上游 MIT 不自动覆盖新增内容，也不等于任何第三方字体、音乐、照片、品牌或声音参考都可商用。

## 反馈

报告问题时，请提供：画风编号或 slug、上游版本、复现/新内容/改编模式、运行命令、实际报错，以及必要的风险时间窗或对照帧。不要提交凭据、私人音色或无授权素材。
