# 让字体、字层和成品对应起来

**Image Typography: Keep the Font and the Lettering Connected**

[图片用字](images.md) · [登记规范](registration.md) · [版本与资料限制](font-evidence.md)

## 浏览器声明的字体，不一定是实际显示的字体

HTML 中的 `font-family` 是选择顺序。字体未加载、家族名不匹配或缺字时，浏览器可能用后备字体补齐；看起来正常并不能证明指定字体实际参与排字。

制作时先等待字体加载完成，再查看文字实际使用的字体；分别检查中文、数字和符号，记录实际字重或可变轴值。字体文件可读取、cmap 有字符，与页面真正采用它是不同条件。完成图应保持字号、画布、缩放与导出参数一致。

本项目五作开场说明使用 Noto Sans SC、CSS 字重 600，保留配方输入为 2.04；菜单 UI 的 450 和 HUD 的静态 500 是另外的用途。不能把同一个家族名当成所有图片的统一字重。

排查后备字体时，可在相同画布与参数下分别渲染指定字体和后备字体，观察字形与布局差异。全图不同时先分离字体、排版、颜色和导出差异；不能仅凭一张截图相似就确认字体身份。

## TTC 索引与可变轴也是配方的一部分

TTC 可以包含多个字体。实际加载的索引决定采用哪套字形和度量，例如历史 BIZ 试样中索引 0 与 1 分别对应等宽和比例宽度。默认加载索引 0 不表示使用了整个集合的所有字体。

登记具体文件、版本、TTC 索引和可变轴值。同名家族、不同发行文件可能有不同字形、字集和许可；从可变字体导出的静态 700 也单独记录原输入和轴值，不与静态 500 或运行时文件混为一项。

## 后续脚本没有加载字体，也可能使用了它的字层

裁切、缩放、着色、透视和合成不会消除原字层的来源。制作器若直接使用旧字幕或字形蒙版，应关联母版的字体与配方，而不是将本图记成“没有字体”。

例如 PF／PM 的选择 HUD 继承装备图的微软雅黑常规体字形蒙版；PM 日历缩略图的提供字幕来自 Noto Sans SC 导出的静态 700，17px、8 倍渲染。它们都需要保留文字母版的身份。

同一图片可以混用字体、原图字形和生成字样，分别登记实际文字层。原字体字层被完整替换时，旧字体转入历史用途；若仍保留一部分，按保留范围继续关联。PF 学校金字后续改为生成字样，与仍用楷体的黑色布幅分别维护。

## 分清文件身份、像素与生成输入

PNG／WebP 文件摘要标识编码文件；解码后的 RGBA 摘要标识像素内容。重新编码可能改变文件字节而保持像素相同；阴影、颜色或透明度域转换也可能改变像素，不能混用这两种摘要证明“同一张图”。

实际成品、字体身份和字层继承关系属于维护数据。某次重放的命令、浏览器环境、像素差统计与失败尝试属于内部记录。公开配方写清适用素材、参数、转换方式和仍缺的资料，逐次执行结果留在本地。

字体排字稿作为生成编辑输入时仍登记字体来源，例如早期 U0483 的 PhotonCN 中文底稿。但生成后的笔画未必还是同一字体；仅写“某字体风格”的提示词，也不等于实际传入了该字体文件。

这些方法帮助维护来源与复现排版，不能代替逐字检查、人工视觉审核或游戏中的实际显示验证。

<details>
<summary><strong>English · Actual fonts, inherited layers and image identity</strong></summary>

Verify the font actually used by the renderer, rather than copying a CSS fallback list. Record collection indices and variation axes. Cropping or compositing a raster text layer preserves its font origin; link it to the source recipe. Separate encoded-file hashes from decoded-pixel hashes, and describe colour or alpha conversions explicitly. A font-rendered draft supplied for image editing remains attributable as an input, without claiming that every generated stroke still belongs to that font. Keep reusable recipes and genuine limitations public; retain individual execution logs locally.

</details>
