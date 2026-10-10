# 本地化制作

[返回首页](../README.md) · [各游戏资产](../docs/research/asset-map.md) · [参与贡献](../docs/project/CONTRIBUTING.md)

从正在做的工作进入。文本和图片各有自己的分步流程，字体、术语和 ParaTranz 各自集中维护，不再增加 `common/` 层。

**先读[翻译最高原则](principles.md)：目标是日译中；日文原版已有英文保留英文，日文只有确实更适合时才译成英文。官方英文版独有素材找对应日语语音听译成中文。正文翻译和图片制作一体适用。**

**大部分日文需要翻译，但不是所有日文都要替换。** 根据内容用途、玩家理解和原作表现区分应译与保留范围；同一段文字或图片也可以部分翻译、部分保留。曲名、署名、原画与日期标记等是帮助理解的例子，新的内容同样按这一原则判断，不能仅因仍有日文就判漏译。

| 工作 | 入口 | 这里维护什么 |
| --- | --- | --- |
| 文本汉化 | **[text/](text/README.md)** | 已使用的两轮翻译流程、01—07 文本规范、新语言指南 |
| 图片汉化 | **[images/](images/README.md)** | 五阶段：提取与分类 → 文案与样式 → 制作 → 自检返修 → 人工审核与交付 |
| 字体 | **[fonts/](fonts/README.md)** | 七作原版／补丁字体、图片用字、来源和对应关系 |
| 术语 | **[glossaries/](glossaries/README.md)** | Muv-Luv通用表、七作专表与君望专表；语境基线放在各作品的`terminology/`中 |
| 协作校对 | **[paratranz/](paratranz/README.md)** | 四个现有项目、参与方式、发布后改文回流与同步 |
| 必要工具 | [tools/](tools/README.md) | 新语言表、字体覆盖、通用图片制作／校验、校对同步 |
| 工具测试 | [tests/](tests/README.md) | 对应上述工具的数据与行为检查，使用合成输入 |

**本项目的文本有 AI 参与，但不是 AI 直出。** 初译后独立对照日文复核，解决疑点、统一术语，完成技术与实机检查；维护者再人工检查、修改错误并复查结果，完成后才发布。玩家下载的版本已经包含发布前的人工修改。ParaTranz 和玩家反馈继续推动后续版本修正，不能反过来理解为“先发布未经处理的生成稿”。详见[文本完整流程](text/workflow.md)。

图片流程采用相同的责任划分：制作方先逐图自检、修正，再交维护者人工审核；审核通过的具体成品才能进入引擎适配和版本制作。视觉检查、人工确认、实机确认和发布分别记录。

## 具体素材放在哪里

| 内容 | 位置 |
| --- | --- |
| 各作译文、图片文案、资源映射和语境基线 | [AGE2/games/](../AGE2/games/README.md)、[rUGP/games/](../rUGP/games/README.md) 下对应作品 |
| FPD／EGPACK／WebP 提取、写回、松散覆盖 | [AGE2 工具](../AGE2/README.md) |
| RIO／CRsa／RUO／ICI、Photon 路由和运行时 | [rUGP 工具](../rUGP/tools/README.md) |
| 历史词库、旧审核批次、来源调查 | [本地化研究记录](../docs/research/localization/README.md)；保留查证价值，不作为当前制作入口 |

原始游戏图片、完整官方文本、私人校对材料、生成缓存和本地审核图库留在获准的制作环境。公开仓库维护方法、可公开的译文／术语、身份记录和工具；成品图和字体的发布范围依各自来源与许可判断。研究记录不会自动升级为现行术语或已发布成果。

<details>
<summary>English · localization and tooling</summary>

Start with [text localization](text/workflow.en.md), [image localization](images/README.md#english-workflow), [font inventory](fonts/README.md), [glossaries](glossaries/README.md), or [ParaTranz collaboration](paratranz/README.md). Engine-neutral authoring stays here; extraction, encoding, runtime binding and packaging stay in AGE2 or rUGP. Historical evidence is under [research](../docs/research/localization/README.md).

Both text and image lettering follow the shared [translation principles](principles.md#english-summary): Japanese to Chinese, retaining English present in the Japanese original. English-edition-only assets are translated from their corresponding Japanese voice, not from the English edition's wording.

Most Japanese text needs translation, but retention depends on function, player understanding and the original presentation. Assess each relevant part; familiar examples are not an exhaustive list of what may remain unchanged.

The maintainer reviews and corrects the release candidate **before publication**. ParaTranz revisions are reviewed, integrated and verified for a later release; an online edit does not update an installed patch.

</details>
