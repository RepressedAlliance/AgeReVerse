# 05 · 人工审核与交付

[上一步](04-self-review.md) · [流程总览](README.md) · [AGE2](../../AGE2/README.md) · [rUGP](../../rUGP/README.md)

**输入：**制作方已自检的最新候选与明确问题。维护者审核、提出修改或直接修正，再复查修改结果。

## 维护者人工审核与修改

送审页应让人直接看图：制作底稿／中文在**相同位置、相同缩放**快速切换，保留放大、拖动、全屏、张数、跳转、分类和“只看修改图”筛选。提供整图与必要细节，另关联实际原意依据和采用的设计，不能只交文字账本或打不开的图片。

按资料用途组织对照：原意提供实际文本、语音或画面及场景；视觉提供选定底稿、借鉴的设计和中文成品；交付提供实际目标与调用。日文版有对应画面时可一并展示，没有时不强制补图或用透明占位充当有效对照。官方英文图可能是底稿、设计依据或仅供比较，准确标明角色；没有找到对应就写“尚未找到”，确认没有才写“不存在”。不能从 `_ja`／`_en` 后缀猜用途，也不要求照搬某版排版。

审核[来源与语言处理决定](../principles.md)。听译展示实际语音与必要片段定位、工作转写和疑点，文字或图内信息提供可核对来源。真正新增信息明确其语源、用途与采用范围，辅助文案核对功能。原意未确认不能因采用了官方模板而通过；原作已有英文、有理由采用的英文与未解决内容分别说明。

同时展示有意保留的原图／原文及范围、理由和确认依据，与待译、待确认分开。维护者按内容用途、玩家理解和原作表现检查保留是否合理，以及同图应译信息是否已处理；新内容采用同一判断方法，不只检查是否符合既有例子。经确认保留项不能被自动“清除日文”再次改写。保留项的最终绑定也须指向正确原图，而非旧中文候选。

疑问集中展示图片、具体位置、已识读原文、拟定中文、不确定原因与建议。能自行解决的问题先解决；已经认可的保留项和效果不用反复询问。需要“通过／待改”或只收建议的形式按本次送审安排选择，不把界面勾选强加给审核者。

**审核确认的是这一次具体成品。** 保存当前采用版本的路径／摘要与修改意见；返修后更新送审和交付引用，避免已批准新图而打包仍取旧候选。未经确认的生成稿不冒充人工定稿。

同时核对本批的[字体使用记录与声明](../Fonts-ThatFitTheGame/registration.md)：采用图和配方对应，混用字体、继承字层和实际后备字没有漏记；字体换过就更新当前对应，并把旧方案标为历史／已替换。公开来源与致谢随素材更新。仅交付烘焙图片和附带字体软件分别处理；可编辑素材或发布包若含字体文件，保留其适用的完整版权与许可。该项随现有审核与交付完成，不增加一个阶段。

## 引擎交付、实机检查与发布

图片制作经人工确认后，再处理游戏集成；这些交付动作合在最后一个阶段，不另增一套做图步骤。

1. 根据真实脚本、GUI／对象引用验证 01 的中文用途与目标规划，确认语言槽、每个资源 ID、路径和覆盖优先级。中文可覆盖 rUGP 现有 `translation` 槽；底稿和写回目标均不由原意语源推定。不按语言后缀排除，也不自动纳入全部官方差分。不能只凭相似文件名选图；内容相似的 `pattern` 与实际 `chr` 资源可能尺寸、用途不同。
2. 通过对应引擎编码、写回和读回验证，确认画布、透明度、有效区域和游戏缩放。原本应全透明的资源不能因名字像标题就塞入 Logo。
3. 在相关菜单、剧情、日期、状态和差分中实机查看：是否被调用，是否偏移、裁切、闪烁、错语言或出现旧图；新增或采用的呈现是否准确可读，字幕分段和显示／清除时机是否对应语音，是否遮挡正文或操作。首次集成按作品覆盖范围检查，后续修改重点复查实际受影响位置。
4. **维护者完成发布前的人工收尾：**修改实机或审核发现的错误、复查修改结果，再制作并发布对应版本。玩家获得的版本已经包含这轮修改。

图片定稿、静态读回、实机确认和发布结果分别记录。不能把“做完图片”当成安装包已发布，也不能让发布后 ParaTranz 校对代替发布前的人工收尾。

**输出：**维护者确认的成品、明确保留项、对应版本的绑定与实机结论，以及实际发布状态。未解决问题返回相关阶段；后续玩家反馈回到文案、成品和源映射修正，再进入下一版。

## English summary

Review the exact candidate with evidence suited to each question: text/audio/
scene for meaning, selected base/borrowed design for appearance, and actual
objects/calls for delivery. Offer aligned base/Chinese switching and useful
detail views, not mandatory Japanese-image pairs. Label missing counterparts
and each official asset's role accurately. Confirm retention, additions and
font use without treating an official template as semantic approval.
Verify every actual target, supported geometry/alpha and engine readback;
Chinese may use rUGP's existing `translation` route. In-game checks cover
information, display/clear timing, voice correspondence, obstruction and states.
The maintainer corrects and verifies issues before publication. Human approval,
integration, in-game verification and release remain distinct facts.
