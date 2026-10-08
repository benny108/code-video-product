# 38 种画风：特点、适用场景与制作指南

原项目：[Changroro/code-video](https://github.com/Changroro/code-video)。
固定参考：[`03da4e3ab149`](https://github.com/Changroro/code-video/tree/03da4e3ab149c4134a9a72eec499e1a2a41601ea) · [README / 原画廊](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/README.md)。

**每种画风都有独立中文制作指南**。点“中文制作指南”查看具体要求，不只是名字和链接：

- 核心辨识：哪些关系让它成为这个画风，而不是颜色相似。
- 适用场景与选型边界：适合什么内容、一个具体选题示例，以及不宜硬套的情况。
- 构图、材质与字体：主次/比例、色彩用途、字体角色和纸/像素/网点等质感。
- 动作、转场与声音：接触因果、镜头/转场机制、原方向的声音与收尾。
- 易错点与处理：该风格特有的简化/脱节/替代风险。
- 本风格验收：应实际看的原尺寸构图、连续动作和声音落点。
- 内容替换边界：新主题能改什么，哪些变化须明确属于改编。

中文指南依据固定版本原文整理，并结合本地退修经验与预防性检查；不是官方译文或完整场景源码。没有新观看的媒体不会冒称已经看过。数值参数随画幅适配，中文字体须实际验证。

以下编号沿用本地38项画廊，不是上游通用编号。先用下表选画风，再到后面的指南目录查看制作要求。

## 特点与适用场景速查

**怎么选：先看内容要完成什么，不先挑好看的颜色。** 需要人物冲突选故事语言，需要证据选调查语言，需要算清一个问题选推导语言，需要展示产品则选展示语言。

特点总结固定版本的参考语言；适用场景与选题是本地选型建议，**不是官方原例剧情**。这些选题不构成新增视频制作任务，也不允许擅自改写原例。真实数字核验来源，自拟数字标注“示例”。

| 编号 | 画风 | 主要特点 | 适用场景 | 一个具体选题示例 |
|---|---|---|---|---|
| 01 | [手绘小剧场](styles/handdrawn.md) | 暖白纸面、细墨线道具与迷你像素角色混搭；用角色和物件的实际互动讲事情。 | 生活矛盾小故事；客户沟通与商业科普；轻松的教育情境 | 早餐店老板为什么不买你的宣传片：先发现他真正缺什么。 |
| 02 | [侦探证据板](styles/detective.md) | 软木证据板、倾斜纸卡和红线关系网；巡查线索、拉远归纳，最后揭晓。 | 原因排查与案例复盘；信息核验与反骗局科普；逐条证据支撑的商业分析 | 报价发出后客户消失了：从三条反馈排查真正原因。 |
| 03 | [像素 RPG 闯关](styles/rpg.md) | 低分辨率游戏场景、装备角色、任务与对话面板；战斗反馈、经验和升级串成成长线。 | 技能成长与阶段挑战；带障碍和奖励的学习故事；个人能力与资源取舍 | 剪辑高手第一次接单：技术能力之外，还得解锁需求沟通。 |
| 04 | [白板手绘课](styles/whiteboard.md) | 实体白板、手与笔的顺序书写、擦除和浅残影；图文随推理逐步建立。 | 概念区别与知识教学；流程拆解；少量公式和因果关系解释 | 一单收了1000元，为什么不等于赚了1000元？逐项画出成本。 |
| 05 | [英雄漫画](styles/comic.md) | 粗黑斜分格、网点纸、夸张姿态、气泡与拟声爆破；动作冲突带动镜头。 | 强冲突故事；夸张喜剧与观点反转；强调行动的短宣传 | 客户的‘再改最后一次’变成改稿怪兽，主角拿交付范围挡住它。 |
| 06 | [简洁品牌动效](styles/motion.md) | 深色舞台、细白线物件、粗几何字与单主强调色；痛点到产品响应的简洁动效。 | 产品价值说明；一项功能的前后对比；服务痛点与解决机制展示 | 每次交片都找不到文件：展示统一版本管理怎样减少重复沟通。 |
| 07 | [界面连续变形](styles/uimorph.md) | 同一个界面元素连续变形；光标交互触发状态变化，首尾可无缝闭合。 | 单一交互流程；界面微动效；产品功能循环演示 | 报价工具由输入工时变成计算、确认和发送状态。 |
| 08 | [热敏小票](styles/thermal.md) | 热敏打印机逐行出纸，带锯齿、条码、总额、红章与撕纸动作；信息像真实小票。 | 账单和成本拆解；订单与消费复盘；项目清单或结算摘要 | 打印一张接单小票：收入减去工时、素材和修改成本，还剩多少？ |
| 09 | [电影预告](styles/trailer.md) | 宽银幕黑边、暖黑与金铜色、居中衬线大字；慢揭晓、光扫与留白呼吸。 | 系列或课程预告；作品主题揭晓；重要里程碑与成果展示 | 用预告片介绍‘从会做视频到拿到第一单’这条学习旅程。 |
| 10 | [工程蓝图](styles/blueprint.md) | 蓝晒底、白色工程线、施工线、尺寸与编号；逐线构建结构和对象关系。 | 系统架构与技术原理；产品结构拆解；生产流程和依赖关系 | 把一次视频交付画成蓝图：需求、脚本、制作、验收如何连接。 |
| 11 | [16-bit 街机](styles/arcade.md) | 16-bit街机开场、投币与选关地图、逐站跳跃、高分和通关；强调短挑战节奏。 | 阶段任务与学习打卡；多步挑战；步骤达成与成果计分 | 接单前的三道关：找到客户、确认问题、交出一份小样。 |
| 12 | [装配说明书](styles/manual.md) | 奶油纸装配手册、粗线、小人物和大步骤号；实体部件与移除量解释机制。 | 操作步骤与方法教程；规则和交付流程；部件、成本或流程的前后对照 | 像装配一件产品那样，依次组好视频服务的范围、修改次数和验收标准。 |
| 13 | [翻页漫画](styles/comicbook.md) | 实体旧漫画封面、书脊与双页分格；镜头阅读画格，卷页推进章节。 | 连续剧情与角色经历；分章节案例故事；需要前后照应的叙事 | 翻开一位创作者的第一单：从自信报价到发现客户理解错了交付。 |
| 14 | [博物馆展览](styles/museum.md) | 夜间展厅、搜索式暖吊灯、低多边形展品与展签；访客在不同房间间移动。 | 有代表物件的概念讲解；成果或作品策展；历史物件与价值来源 | 参观信任展厅：样片、履约记录和客户评价各自证明什么。 |
| 15 | [绘本故事](styles/storybook.md) | 木桌上的皮面绘本，圆窗插画、柔和角色与衬线叙述；物理翻页和温柔节奏。 | 儿童与亲子故事；温和的情绪和成长叙事；低压力的教育启蒙 | 小熊发了报价却没收到回复，它先问清情况，而不是立刻责怪自己。 |
| 16 | [体育转播](styles/sports.md) | 球场、常驻比分与LIVE角标、双方配色、跑道回放和MVP；对比像一场比赛。 | 明确指标的方案对比；A/B实验结果；团队挑战与阶段成绩 | 按工时报价和按交付包报价对阵：用示例比较返工时间和结余。 |
| 17 | [粒子动效](styles/particles.md) | 发光粒子从流动中聚成字、数或图标，再变形或散开；形状由粒子真正构成。 | 片头与品牌揭晓；少量关键数字；汇聚、分散或形成的抽象概念 | 零散能力粒子汇成一个清楚的服务名称，作为产品化章节的开场。 |
| 18 | [机械翻牌](styles/splitflap.md) | 铁路机械看板，上下字片沿铰链逐列翻动，配合时钟、状态灯与机械声。 | 排期与进度公告；状态更新与结果揭晓；短列表和时间表 | 接单排期看板依次翻出：待确认、制作中、待验收、已交付。 |
| 19 | [科技发布会](styles/brand-samsung.md) | 黑色科技揭晓、反射与光扫，转白色规格段；电蓝强调和大参数形成发布会感。 | 智能设备与硬件发布；科技工具功能介绍；有明确规格的产品展示 | 展示自有录音设备或剪辑工具：逐项说明输入、处理和输出能力。 |
| 20 | [设计文档驱动](styles/designmd-stripe.md) | 按实际设计文档构建页面系统；画廊例为斜切渐变、左标题与右侧浏览器预览。 | SaaS和网页产品发布；有设计系统的品牌说明；支付或开发者工具演示 | 依据自己报价网站的DESIGN.md，演示客户填写需求到得到方案。 |
| 21 | [新闻播报](styles/news.md) | 深蓝播报台、雷达地球、逐级地图与数据卡；频道标、时钟和新闻下栏常驻。 | 已核验资讯摘要；事件与数据快报；栏目式科普播报 | 客户采访简报：分别呈现三家店提出的需求，再给出采访范围。 |
| 22 | [剪贴簿](styles/scrapbook.md) | 牛皮纸手账、真实照片拍立得、胶带与手写笔注；制作痕迹和里程碑形成记录感。 | 项目制作过程；旅行与生活回顾；团队复盘和成长记录 | 用授权照片、需求便笺和样片截图，记录第一次到店找客户的经过。 |
| 23 | [撕纸拼贴](styles/collage.md) | 撕纸纤维边、水彩纹理和柔影；纸片逐块拼成景物，画面具有手作层次。 | 自然与环保叙事；城市文化和活动介绍；可用象征景物表达的故事 | 街区纸片拼成小店生态：顾客、店员、商品和服务相互连接。 |
| 24 | [沙画](styles/sand.md) | 暖光台上的深褐沙剪影，颗粒吹散后重新成形；用形态变迁串联时间。 | 年代与城市变迁；人物成长和情感故事；历史概念的演化 | 从口头约定到写下服务合同，用沙画展示一段合作关系的变化。 |
| 25 | [霓虹招牌](styles/neon.md) | 暗砖墙、实体发光灯管、通电闪亮与湿地反射；短字和图标像夜间招牌。 | 夜间活动和演出开场；店铺短招牌；章节标题与短口号 | 用一句‘先谈范围，再谈价格’点亮谈判章节的开场。 |
| 26 | [暗色媒体](styles/brand-spotify.md) | 炭黑内容库、多彩封面和卡点轮播；紧字距标题与绿色主操作区分内容和动作。 | 播客与课程库；节目推荐和内容策展；媒体产品展示 | 把自有案例课按找客户、定价、交付三个主题策展成可浏览的内容库。 |
| 27 | [电视购物风](styles/infomercial.md) | 饱和放射背景、夸张喊字与前后对比；价格、电话、购物台角标推动喜剧节奏。 | 复古广告戏仿；消费心理与促销机制科普；夸张的产品创意介绍 | 一件东西从标价到‘限时优惠’，演示价格锚点如何影响观感。 |
| 28 | [CRT 终端](styles/terminal.md) | 绿色磷光CRT、命令输入、日志滚动、进度与块字标题；执行顺序决定节奏。 | 开发者工具介绍；自动化流程说明；编程和复古计算机科普 | 展示视频批处理队列：逐项校验素材，再渲染、导出并检查结果。 |
| 29 | [竞速奢华](styles/brand-ferrari.md) | 黑白编辑式展示、宽字距大写、方角与克制红线；慢移与驻留突出材料和工艺。 | 高端机械与汽车展示；材料工艺说明；精品设计和定制服务 | 展示一项精品视频服务的镜头、调色和声音工艺，而不是只宣称高级。 |
| 30 | [运动力量](styles/brand-nike.md) | 黑白强对比、窄粗巨字冲击、速度痕和节拍硬切；主体动势形成力量感。 | 训练与行动挑战；赛事和运动产品宣传；有实际行动过程的号召 | 三天做出第一份能展示的样片：拍、剪、测试的动作连成训练节奏。 |
| 31 | [数学推导](styles/mathlecture.md) | 近黑讲义、逐项公式、编号推导和坐标图；高亮结果由计算过程自然得到。 | 数学与算法讲解；成本、利润和盈亏平衡；可复算的模型权衡 | 用自拟成本算清：一个服务包卖多少钱，才能覆盖工时和固定支出？ |
| 32 | [纪录片](styles/documentary.md) | 黑场、档案纸、章节与引用、单重点数据；慢溶解和留白让证据落稳。 | 历史与社会问题梳理；商业案例深度复盘；有来源的研究与调查故事 | 一家公司订单很多却周转困难：依据公开资料追踪现金流的时间差。 |
| 33 | [地铁路线](styles/transit.md) | 彩色地铁线路、站点与换乘，列车沿真实路径逐站前进；空间路径解释步骤关系。 | 学习与职业路径；项目里程碑；客户流程和决策分支 | 从客户咨询到最终交付：每站标出该确认的事项和可分流的问题。 |
| 34 | [天气预报](styles/weather.md) | 蓝黄天气播报包装、雷达、温度计与风速仪、多日卡；仪表和天气图标共同解释趋势。 | 气象科普与核验后的预报；有数据的阶段趋势；明确标注的经营趋势隐喻 | 把店铺淡旺季做成经营天气图，标明是假设示例而不是真实预报。 |
| 35 | [动态歌词](styles/lyric.md) | 每句配解释图、关键词按时间表点亮；重复段落复用图形并换强调色。 | 知识节奏记忆；原创教育歌词的屏幕可视化；短概念的重复复习 | 用原创短句和器乐节奏复习：收入、成本、利润三者怎样对应。 |
| 36 | [节拍同步](styles/beat.md) | 真实素材墙、片段筛选、透视轮播和产品界面；动作与切镜跟实际音轨节拍。 | 创作者作品集；剪辑与AI视频工具演示；授权素材精选和产品宣传 | 用自己的原片与成片片段卡点对照，展示剪辑服务究竟改变了什么。 |
| 37 | [极简展台](styles/brand-apple.md) | 白黑极简展台、隔离产品与柔影、渐变名称和圆角功能格；慢而柔的揭晓突出主体。 | 精品硬件展示；精致软件功能介绍；聚焦少数卖点的自有产品发布 | 把自己的报价工具当作一件产品，先揭晓主体，再演示三个关键功能。 |
| 38 | [自由混合风格](styles/free.md) | 先定义本次材质、构图、字体和运动规则的自由设计模式；画廊例是纸面绘图头，并非固定模板。 | 没有现成预设的新品牌；用户自带明确参考；具有统一视觉规则的实验主题 | 若明确采用画廊绘图头语言，可让笔头逐线画出一张服务现金流示意图。 |

### 容易混淆的几组

- **01 手绘 / 04 白板**：手绘用人物做事，白板用书写过程推理；不能都做成白底字幕。
- **03 RPG / 11 街机**：RPG偏角色、装备和成长；街机偏选关、短挑战和积分。
- **05 英雄漫画 / 13 翻页漫画**：前者强调动作冲突；后者强调实体书、分格阅读和章节。
- **22 剪贴簿 / 23 撕纸拼贴**：前者记录照片和制作痕迹；后者用纸片本身拼出景物。
- **19 科技发布 / 29 竞速奢华 / 30 运动力量 / 37 极简展台**：分别是光扫与规格、慢工艺与方角、冲击与快切、柔影与慢揭晓；不是换一个logo就等价。
- **21 新闻 / 32 纪录片 / 34 天气**：分别是快报、证据叙事、趋势与仪表；包装不能把模拟内容变成真实报道。
- **35 动态歌词 / 36 节拍同步**：前者逐词配解释图；后者用实际素材和音乐节拍编排切镜。
- **20 设计文档驱动 / 38 自由模式**：前者服从真实设计系统；后者先确定本次设计规则。都不是一套可随意套用的固定美术。

粒子、霓虹和预告等语言可先作为短片头或重点段使用，信息密集时结合本画风可读的说明层，不硬把所有内容塞成同一种一分钟结构。品牌名仅指参考设计语言，不表示获得品牌授权或合作。

## 38种画风指南目录

| 编号 | 画风 | 中文制作指南 | 核心注意事项（详见指南） | GitHub 原指南 | 原动图 |
|---|---|---|---|---|
| 01 | 手绘小剧场 · `handdrawn` | [中文制作指南](styles/handdrawn.md) | 不能暖色底加通用方块人就算还原；角色像素与细墨道具有意混搭，不是所有元素都像素化。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/handdrawn.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/handdrawn.gif) |
| 02 | 侦探证据板 · `detective` | [中文制作指南](styles/detective.md) | 旋转卡片的钉位和线端必须共用world anchor，不能悬空、弯曲或连错角。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/detective.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/detective.gif) |
| 03 | 像素 RPG 闯关 · `rpg` | [中文制作指南](styles/rpg.md) | 不能高清大矩形人物加CRT冒充像素美术；像素层禁平滑插值和半格落点。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/rpg.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/rpg.gif) |
| 04 | 白板手绘课 · `whiteboard` | [中文制作指南](styles/whiteboard.md) | 全句fade-in加摆动手不是写字；不得多处同时出字却只有一个远处笔尖。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/whiteboard.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/whiteboard.gif) |
| 05 | 英雄漫画 · `comic` | [中文制作指南](styles/comic.md) | 不和comicbook混淆：这里强调英雄行动/斜分格，不强套居中实体双页2×2系统。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/comic.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/comic.gif) |
| 06 | 简洁品牌动效 · `motion` | [中文制作指南](styles/motion.md) | 品牌原站浅色也不能把该画风改成白底UI；品牌只进主强调/标志。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/motion.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/motion.gif) |
| 07 | 界面连续变形 · `uimorph` | [中文制作指南](styles/uimorph.md) | 切掉旧卡再pop新卡不是morph；各状态应共享边界/形变参数。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/uimorph.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/uimorph.gif) |
| 08 | 热敏小票 · `thermal` | [中文制作指南](styles/thermal.md) | 完整纸片连字一次浮上来不算打印；用纸局部坐标和机槽clip控制揭示。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/thermal.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/thermal.gif) |
| 09 | 电影预告 · `trailer` | [中文制作指南](styles/trailer.md) | 大光晕不能把衬线轮廓冲白；来源很灰也须在实际MP4可读。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/trailer.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/trailer.gif) |
| 10 | 工程蓝图 · `blueprint` | [中文制作指南](styles/blueprint.md) | 主线/施工线不能同粗同亮，编号不是无关装饰；尺寸端点须绑定对象几何。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/blueprint.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/blueprint.gif) |
| 11 | 16-bit 街机 · `arcade` | [中文制作指南](styles/arcade.md) | 不复制RPG钢框/剑与史莱姆替代街机选关语言；像素层禁任意平滑和非整数坐标。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/arcade.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/arcade.gif) |
| 12 | 装配说明书 · `manual` | [中文制作指南](styles/manual.md) | 三组价签+小收据不能改成三个巨大收据；比“道具类型差不多”更严格核对组合。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/manual.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/manual.gif) |
| 13 | 翻页漫画 · `comicbook` | [中文制作指南](styles/comicbook.md) | 不和英雄comic混同：原主要运动是读实体刊物，不强迫每格角色大动作。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/comicbook.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/comicbook.gif) |
| 14 | 博物馆展览 · `museum` | [中文制作指南](styles/museum.md) | camera offset与world灯/人分开；spotX=camera+常数会让灯屏幕锁定，丢失搜索。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/museum.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/museum.gif) |
| 15 | 绘本故事 · `storybook` | [中文制作指南](styles/storybook.md) | 白卡左右摆两栏不是绘本；圆窗与人物不能用通用大头像取代。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/storybook.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/storybook.gif) |
| 16 | 体育转播 · `sports` | [中文制作指南](styles/sports.md) | 常驻score bug不能跟场景移走；最大值不一定是优胜，成本/耗时需按指标方向判断。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/sports.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/sports.gif) |
| 17 | 粒子动效 · `particles` | [中文制作指南](styles/particles.md) | 太少点导致缺笔画，太强bloom冲成白块；增加点数不是唯一办法，先改采样/字重/停留。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/particles.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/particles.gif) |
| 18 | 机械翻牌 · `splitflap` | [中文制作指南](styles/splitflap.md) | 随机换字符不是机械翻牌；上下裁片、铰链遮挡和新旧字层次要一起算。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/splitflap.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/splitflap.gif) |
| 19 | 科技发布会 · `brand-samsung` | [中文制作指南](styles/brand-samsung.md) | 不混Apple蓝CTA/bento当本preset；蓝不是背景满铺，反射不是第二个不变产品剪影。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/brand.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/brand-samsung.gif) |
| 20 | 设计文档驱动 · `designmd-stripe` | [中文制作指南](styles/designmd-stripe.md) | 缺DESIGN.md/CSS/可核验截图时先补参考，不能拿Apple等preset补上再称Stripe。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/brand.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/designmd-stripe.gif) |
| 21 | 新闻播报 · `news` | [中文制作指南](styles/news.md) | 三张不相关地图轮换不是逐级定位；主持不必强加夸张口型，镜头语法不能变手绘故事。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/news.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/news.gif) |
| 22 | 剪贴簿 · `scrapbook` | [中文制作指南](styles/scrapbook.md) | 斜白卡加手写标题不等于手账，图像依据和固定痕迹不能丢；重要截图不能裁掉关键信息。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/scrapbook.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/scrapbook.gif) |
| 23 | 撕纸拼贴 · `collage` | [中文制作指南](styles/collage.md) | 只有背景纸纹而所有物件都干净矢量是伪材质；每块撕边/白纤维/水彩斑都须稳定。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/collage.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/collage.gif) |
| 24 | 沙画 · `sand` | [中文制作指南](styles/sand.md) | 只叠噪点的矢量黑轮廓不够，边缘/烟/转场要用粒度表现。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/sand.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/sand.gif) |
| 25 | 霓虹招牌 · `neon` | [中文制作指南](styles/neon.md) | glow过强吞笔画，应分外halo/中亮管/白芯；反射不是一份等亮倒置副本。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/neon.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/neon.gif) |
| 26 | 暗色媒体 · `brand-spotify` | [中文制作指南](styles/brand-spotify.md) | 没封面/内容系统、只有暗卡+绿色字是表面化；封面多彩不等于给UI部件多彩gradients。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/brand.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/brand-spotify.gif) |
| 27 | 电视购物风 · `infomercial` | [中文制作指南](styles/infomercial.md) | 不把兴奋做成整片统一抖动，星光不要盖住价格；ticker是稳定播报层，不随产品弹跳。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/infomercial.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/infomercial.gif) |
| 28 | CRT 终端 · `terminal` | [中文制作指南](styles/terminal.md) | 日志未完成先显示OK，进度100%时仍标失败/加载均不一致；虚构输出不能冒称跑过真实程序。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/terminal.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/terminal.gif) |
| 29 | 竞速奢华 · `brand-ferrari` | [中文制作指南](styles/brand-ferrari.md) | 满屏大红或红蓝赛博光破坏“红色节制”；把Ferrari和体育sports/Nike混合将改变速度语言。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/brand.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/brand-ferrari.gif) |
| 30 | 运动力量 · `brand-nike` | [中文制作指南](styles/brand-nike.md) | 标题震动但没有slam运动不是力量感；过度blur吞字，应在落定时恢复清晰。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/brand.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/brand-nike.gif) |
| 31 | 数学推导 · `mathlecture` | [中文制作指南](styles/mathlecture.md) | 引理只是可视结构，不能把未经证明观点写成数学定理；算式的收益/成本单位应一致。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/mathlecture.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/mathlecture.gif) |
| 32 | 纪录片 · `documentary` | [中文制作指南](styles/documentary.md) | 奶油卡片不带grain/落稳就不像档案；全柱都accent会破坏焦点。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/documentary.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/documentary.gif) |
| 33 | 地铁路线 · `transit` | [中文制作指南](styles/transit.md) | 列车直线插值可能切过折线路外，需按实际path位置计算；路径/站坐标不能分两套。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/transit.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/transit.gif) |
| 34 | 天气预报 · `weather` | [中文制作指南](styles/weather.md) | 一排滑入普通卡不够，应有真实天气/表盘语法；图标不能和headline争重。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/weather.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/weather.gif) |
| 35 | 动态歌词 · `lyric` | [中文制作指南](styles/lyric.md) | 一句抽象励志字幕加音乐不是教育lyric；每句应有模型/事实并有来源。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/lyric.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/lyric.gif) |
| 36 | 节拍同步 · `beat` | [中文制作指南](styles/beat.md) | 没素材就用灰占位并称完整是不合格；需取授权素材或明确用户允许的程序内容改编。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/beat.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/beat.gif) |
| 37 | 极简展台 · `brand-apple` | [中文制作指南](styles/brand-apple.md) | 白底+粗字不够，要有主体材质/柔影/层次；不能跨入Samsung反射光扫/Spotify素材墙。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/brand.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/brand-apple.gif) |
| 38 | 自由混合风格 · `free` | [中文制作指南](styles/free.md) | 用户指定free例并不授权换新主题/随便增品牌；重建例与新风格创作先分清。 | [原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/free.md) | [GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/free.gif) |

## 使用与来源边界

- 只加载用户指定的中文指南与原参考，不把所有画风规则混到一集。`style_brief.py` 已接入这些文档，返回工作包时附选中画风的中文制作要求。
- 5个品牌preset各有中文指南，虽然上游共用brand.md；designmd-stripe是设计文档驱动，不是第六个固定preset。
- free没有普遍固定造型；其指南分别说明自定设计与复现当前画廊绘图头示例。
- 有原GIF不等于有官方完整MP4或完整场景源码；本地复现不能冒称原作者完整源片。
- [完整制作流程](../SKILL.md) · [历史风险速查](style-risk-map.md) · [机器可读索引](style-catalog.json)
