# 20 · 设计文档驱动（designmd-stripe）

[GitHub 原项目](https://github.com/Changroro/code-video) · [固定版本原指南](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/references/styles/brand.md) · [原 GIF](https://github.com/Changroro/code-video/blob/03da4e3ab149c4134a9a72eec499e1a2a41601ea/docs/gallery/designmd-stripe.gif)

依据上游指南整理的中文制作要求；易错与验收部分含本地经验及预防建议，不是官方场景源码。参数按参考画幅理解，中文字体须实际验证覆盖与授权。

## 核心辨识
设计文档驱动，不是第六个硬编码品牌preset。此画廊GIF所见：暖粉/奶白/紫渐变斜切hero、顶部导航、左大标题与右侧浏览器预览卡逐步建立。

## 适用场景与选型边界
- **适合**：SaaS和网页产品发布；有设计系统的品牌说明；支付或开发者工具演示。
- **新内容选题示例**：依据自己报价网站的DESIGN.md，演示客户填写需求到得到方案。
- **选型边界**：不是固定Stripe预设；缺设计文档或可核验页面时不能声称精准还原，也不能混用其他品牌tokens。

这些用途是基于画风机制的选型建议，不是上游官方用途或原例剧情。复现原例时仍保持原主题；做新内容时再采用适合的选题。

## 构图、材质与字体
- 精确颜色/字号/tracking/圆角从用户指定DESIGN.md或真实参考抽取；本地GIF只能证明可见形态，不能凭空宣称某套Stripe官方token。
- 当前画廊例是斜分色域和白区域、细导航、左文右预览/时间线、紫CTA的网页发布布局，不应混成Samsung反射黑台。

## 动作、转场与声音
- 文档先映射bg/bgAlt/dark/ink/accent/surface/spacing/components，再按其中motion规则设计动画。
- 若复现本例，渐变场、headline、预览内部内容/时间线与CTA依次出现；预览窗口不是一张静态截图漂移。
- brand指南未规定固定配乐；保留原媒体实际声音，另配音须记录改编。

## 易错点与处理
- 缺DESIGN.md/CSS/可核验截图时先补参考，不能拿Apple等preset补上再称Stripe。
- 仅抓多彩渐变而丢导航、斜切分区、文字密度/控件圆角是表面化；文档明确禁止项也须落实。

## 本风格验收
- 逐token对源文档记录来源；与原截图比斜边、两栏比例、导航和CTA。
- 查实际预览状态变化/渐变裁切/文字对比；未获文档的token标未知，不虚称已精确还原。

## 内容替换边界
新品牌使用它自己的DESIGN.md；复现本画廊保持其可见网页语法，不能把文档驱动理解成自由混用品牌。

[返回38种画风总索引](../style-catalog.md) · [通用验收](../acceptance.md)
