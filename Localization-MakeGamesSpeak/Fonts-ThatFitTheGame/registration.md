# 每做一批图，把用字一起留下

**Register the Font, Keep the Image Reproducible**

[字体入口](README.md) · [现有使用表](images.md) · [来源与许可](attribution.md) · [图片五阶段](../Images-MakeItLookNative/README.md)

从新制作和返修开始，每批图片都登记实际用字，并把可公开的对应关系汇总到本目录。优先复用游戏现有配方和素材清单，同组共享一条样式记录、单图只写例外；不要求每张重复填一套表，也不另加一个制作阶段。

## 选样时记来源，交付时记实际采用

| 现有阶段 | 必须留下的内容 |
| --- | --- |
| 02 文案与样式 | 字体名称、作者／上游、具体文件和版本、文件摘要、许可原文或授权依据、是否修改／补字／子集；TTC 记录实际字体索引，可变字体记录轴值 |
| 03 制作／返修 | 游戏、素材组及资源 ID、用到的字体目录 ID、排字配方和当前图；同图混用、后备字体实际补了哪些字、局部字体变化分别记录 |
| 05 人工审核与交付 | 实际采用的成品与对应配方，来源表同步更新；试样、被替换、人工确认、实机确认、发布版本分别如实记录；携带字体文件时一并核对适用声明 |

新字体先在 [catalog.json](catalog.json) 登记一次，再在 [image-font-usage.json](image-font-usage.json) 或对应游戏公开清单中引用；来源、作者与用途补入[图片字体致谢](attribution.md)。已登记字体直接引用，不反复复制许可证说明。若配方目前只在本地，公开游戏／素材范围、字体身份和证据摘要；本地绝对路径、私人审核对话和原游戏资源不上传。

发布时以**实际打包的图片**关联已采用配方和字体 ID，记录版本、资源路径与成品摘要；同字节副本共用条目即可。静态审核页中的“未安装”只是当时的状态，后来发布采用后要同步更新。现有[AGE2](age2-released-image-fonts.json)和[Photon](photon-released-image-fonts.json)逐图表提供这种对应方式；[在制表](unreleased-image-fonts.json)继续独立维护，不能靠复制候选清单推定发布内容。

只有候选时可以提交候选，并写明待确认项。缺来源的旧记录标明缺口；实际分发字体前必须解决其授权与声明问题。不要为补表猜测字体、伪造批准，或把文档完善变成所有普通 PR 的新门槛。

## 一条素材组记录应回答什么

下面是已有使用表的扩展示例，示例 ID 不代表真实素材。排版参数仍可留在游戏现有配方中，通过 `recipe` 关联，无需复制整个制作工程：

```json
{
  "id": "example-menu-family",
  "games": ["tda00"],
  "materials": ["example-resource-id"],
  "font_ids": ["image:noto-sans-sc-vf"],
  "recipe": "project-relative-recipe.json",
  "typography": {"axes": {"wght": 450}, "size": 24},
  "method": "font-typesetting",
  "production_state": "candidate",
  "release_adoption": "not-released",
  "evidence": [],
  "note": "Example only; replace with actual material and review evidence."
}
```

实际配方再保留字距、行距、基线、描边、阴影、透视和输出参数。声明过的后备字体不一定真正参与排字；实际使用了哪款、用于哪些文字才进入本图的使用关系。仅作为审核页标题、对照表标签的字体与游戏成品分开，不把浏览器 CSS 后备列表当成真实用字证据。

同名家族可能有不同授权的发行文件，许可跟随实际输入及其来源，不能用另一套发行的 OFL 页面替代 Windows 文件的许可声明。成品摘要注明对象是 PNG／WebP 文件字节，还是解码后的 RGBA 像素；两种摘要不能混用。复制旧配方后也要核对字体字段是否仍对应实际字层。

## 换字体或换版本时

替换文件、字重、字形来源或后备字体后，更新当前配方和受影响素材对应；旧记录标为历史／已替换，保留替换关系。完成图若混有继承的旧字层，也保留这些层的字体来源。新批准的图要成为交付所指的版本；字体换了以后至少复查本图及相关差分的缺字、简体字形、排版和视觉效果，不重测无关游戏。

提供的 PNG 字层、手工合成图和缩略图也追到文字母版：只做裁切／缩放／合成不会消除原字体来源。字体名相同但文件不同仍分别登记，例如原版美呗与补字后的运行时文件、Noto 可变字体与导出的静态 700；静态导出记录原输入、轴值和处理方式。若字体排字后来完全被生成字样替换，保留旧输入的历史状态，再核对生成时实际提供的参考图，不能自动认为旧字体仍被采用。

生成／手绘字样填写 `generated-lettering`、`hand-painted` 等实际方式，原图搬字填写 `original-glyph-reuse`。没有字体输入就写不适用；使用字体作底稿、参考图或后续补笔则登记该字体和用途，不能统一写成“AI 生成”来略去排字来源。

## 公开前的声明

图片使用表和致谢随本次素材更新。若交付物含字体二进制或可编辑工程内的字体，附其实际版权／完整许可，核对衍生字体改名与分发条件；仅交付烘焙图片时遵守对应图形使用许可，并保留本项目的来源登记。详见[许可区别](attribution.md#图片致谢和随包许可证分别处理)。

<details>
<summary><strong>English · Apply this within the existing workflow</strong></summary>

Record source, authorship, exact font identity, license and modifications during style selection. Link game material IDs to the fonts actually used, including mixed layers and real fallback use. At human review and delivery, update the selected recipe, credits and adoption status; mark superseded trials rather than silently replacing their history. Keep private paths and game artwork out of the public register. Ship the actual copyright and full license notices whenever font software is included. Generated or painted lettering has no invented font identity, but any font used as its input or base remains attributable. Reuse existing group recipes; this adds records to the five stages, not another stage or a blanket PR gate.

</details>
