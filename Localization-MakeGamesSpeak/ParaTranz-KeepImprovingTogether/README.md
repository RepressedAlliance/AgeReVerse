# ParaTranz 多人校对｜一起把译文磨得更好

**ParaTranz Collaboration: Keep Improving the Translation, Together**

[返回本地化](../README.md) · [文本流程](../Text-AITranslationWorthReading/README.md) · [维护者同步说明](sync.md)

<details>
<summary><strong>English · Keep Improving the Translation, Together — expand here</strong></summary>

These four existing projects collect Japanese-to-Chinese corrections and player findings. The maintainer has already reviewed and corrected a patch before release. Further ParaTranz edits are reviewed, synchronized to maintained game tables, verified and included in a later package. An online revision does not update an installed patch. Use the matching game's glossary and preserve IDs/control codes; images and fonts follow separate authoring workflows.

Community proofreading shares the current text, source context and discussion:

1. Locate the game, file and entry, then read the surrounding scene and existing notes.
2. Consult the matching game's approved terminology and contextual baseline. Candidates and unresolved questions remain distinguishable from adopted decisions.
3. Explain the problem, propose a correction and provide the relevant evidence. Record differing interpretations for maintainer review rather than silently overwriting a disputed choice.
4. Trace adopted changes to related occurrences, integrate them into maintained source tables, and verify the affected structure or display before a later release.

You can contribute a single well-explained correction. If you cannot read Japanese, reports of typos, awkward wording, image remnants, display or installation problems are also welcome through QQ group **273626767** or the [issue guide](../../docs/player/README.md#排错与反馈). For maintainers, [sync.md](sync.md) documents the current pull-only mapping and conflict handling.

</details>

一部作品的译文，可以由更多读过它的人一起打磨。ParaTranz 提供共同查阅原文、译文、上下文和讨论的地方；参与者可以从一句台词开始校对、改错或补充判断依据，不需要先学会编程。

发布前，我们完成文本初译、独立日文复核、技术与实机检查，最后由维护者人工检查、修改错误并复查，再发布版本。**玩家下载的文本已经包含这轮人工修改。** ParaTranz 通常接在发布后，让其他参与者继续对照日文校对、改错和讨论术语；在制作品提前开放也不表示已有安装包。

## 加入哪个项目

| 作品 | 校对入口 | 可以一起维护的内容 |
| --- | --- | --- |
| TDA00–03 | **[加入 TDA 校对](https://paratranz.cn/projects/19505)** | 四作正文，及姓名／UI 补充资料 |
| 帝都燃烧 | **[加入帝都燃烧校对](https://paratranz.cn/projects/20659)** | 正文、姓名、选项和界面 |
| PF／光子之花 | **[加入光子之花校对](https://paratranz.cn/projects/20660)** | 本作章节及系统中文表 |
| PM／光子旋律 | **[加入光子旋律校对](https://paratranz.cn/projects/20661)** | 本作章节及系统中文表 |

现有四个线上项目在 2026-10-05 逐个核对过；文件映射、当日计数及同步范围见[维护者同步说明](sync.md)，以项目实际文件为准。平台翻译率或“已审核”计数不能反推发布前维护者是否修改过文本。TDA 的原生空结构保持空白，不当成漏译填充。

君望本篇与附加篇仍在制作和文本审核，尚未开放公开全文 ParaTranz 校对，也未接入这四个项目的同步范围；[状态入口](../../AGE2/games/kiminozo/README.md)。

## 怎么参与

如果你看得懂日语，愿意对照原文校对、修改译文或讨论术语，欢迎进入对应项目。可以从熟悉的一句台词或一个场景开始，不必一次承担整章。登录后从项目文件进入；需要参与权限时联系维护者。

结合前后文修改，保留稳定词条身份、必要控制符和已确认术语；使用[通用＋本作术语](../Glossaries-KeepItConsistent/README.md)，不套用其他作专表。难以确定的内容提出具体疑问，说明场景与依据。不要仅为换一种说法重写已经确认的文风。

## 多个人怎样参考、讨论和修改同一份文本

1. **先定位与回读。** 找到作品、章节／文件和词条，连同前后文核对原文、当前译文、备注及已有讨论。必要时补充游戏场景或截图，避免只看单句。
2. **参考同一套采用决定。** 查本作[术语表与语境基线](../Glossaries-KeepItConsistent/README.md#各作术语表与基线)，区分已确认译法、候选和待核问题；人物关系与语气同样需要上下文支持。
3. **给出可讨论的修正。** 说明哪里不准确或不通顺、建议怎样改、依据是什么。读不准时提出具体疑问；意见不一致时保留不同理由，交维护者确认采用方案。
4. **把一项修正落实到相关位置。** 同一问题可能还出现在别处。按[修改反查方法](../Text-AITranslationWorthReading/07-change-impact.md)查找关联台词、称谓和术语，逐项判断，保留有依据的场景差异。

参与者不必一次处理整章。一个能定位、能说明依据的小修正，就能帮助后续维护；采用结果与后续同步由维护者协调。

**看不懂日语也欢迎反馈。** 错字、漏翻、读起来不自然、图片残字、显示或安装问题，都可以加入 **QQ 群 273626767**，或通过[GitHub 反馈入口](../../docs/player/README.md#排错与反馈)说明作品、补丁版本、场景和现象，附截图更方便定位。

## 修改如何进入玩家版本

ParaTranz 修订 → 维护者确认 → 同步回本作可维护中文表 → 相关结构／术语／显示检查 → 打包与人工收尾 → 后续版本发布。

在线修改、GitHub 同步和玩家安装包更新是不同步骤。同步工具不自动翻译、不改在线审核状态、不覆盖双边冲突，也不自动合并或发布。图片、字体和资源构建不由 ParaTranz 同步处理。

这里的四个子目录保存现有映射和摘要基线：它们用于关联词条、发现双方修改冲突，并非禁止改中文的白名单。日常参与从上方项目链接开始；维护者操作见[同步说明](sync.md)。
