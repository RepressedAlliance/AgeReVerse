# 05 · 人工审核与交付

[上一步](04-self-review.md) · [流程总览](README.md) · [AGE2](../../AGE2/README.md) · [rUGP](../../rUGP/README.md)

**输入：**制作方已自检的最新候选与明确问题。维护者审核、提出修改或直接修正，再复查修改结果。

## 维护者人工审核与修改

送审页应让人直接看图：制作底稿／中文在**相同位置、相同缩放**快速切换，保留放大、拖动、全屏、张数、跳转、分类和“只看修改图”筛选。提供整图与必要细节，另关联实际原意依据和采用的设计，不能只交文字账本或打不开的图片。

按审核者实际设备交付能打开的材料：可访问的页面入口，或包含所需图片、说明和依赖的独立附件；维护者电脑上的绝对路径、`localhost` 链接不能当作他人的访问入口。交付前确认接收方式可用，手机审核时也要能加载图片。现有工具缺少部分展示或反馈能力时，可配合图片附件、说明和独立意见文件，不宣称工具已具备这些功能。

按资料用途组织对照：原意提供实际文本、语音或画面及场景；视觉提供选定底稿、借鉴的设计和中文成品；交付提供实际目标与调用。日文版有对应画面时展示，没有时不强制补图或用透明占位充当有效对照。官方英文图通常用于对照或设计参考；确需复用其具体画布或模板时，说明用途与理由，并准确标明角色。没有找到对应就写“尚未找到”，确认没有才写“不存在”。不能从 `_ja`／`_en` 后缀猜用途，也不要求照搬某版排版。

**送审默认按“官方日文 → 官方英文（有则提供）→ 之前的中文（有则提供）→ 当前中文”组织准确对照。** 官方英文即使仅供参考也保留入口；已有旧中文时，提供本次修改前的对应版本，让审核者看清改动与是否引入新问题。首次制作没有旧中文、没有对应英文图时不强求，也不用其他图片凑数。每个视图标明角色及对应版本；旧中文区分已发布、已确认或未确认候选，当前中文标明本次送审版本，不能把旧稿显示成当前成品。

对照图旁附上**面向审核者的简短说明**，逐图或按同类素材组说明：图用在哪里；这次改了哪些文字或区域；为什么这样翻译、排版或返修；哪些内容有意保留及理由；还有什么不确定、需要人判断。说明直接指向图中位置，可用“左下角地名”“第二行字幕”等易懂表述；同组共性解释一次，单图例外另写。返修明确旧中文的问题和当前修正，首次制作说明关键处理。不只给文件名、状态码或制作流水，也不要求审核者翻聊天记录才能理解。当前中文仍是候选时明确写“待人工确认”，说明不能代替查看实际图片。

动态图层提供实际合成预览，连续帧提供可播放序列或片段及必要定位，让人看到文字的出现、保持、切换与消失；静态对照仍用于核对细节。不能只给抽出的某层或几张截图，就请人确认整个动态效果。

若确需复用英文版画布或模板，提供所复用部分／中文对照，说明具体用途与理由，另关联日文原意依据；没有同形式日文图时，展示实际日文文本、日语语音或其他画面依据及场景，并说明缺少哪种对应。日文图只有透明占位的字幕则提供日语语音，不用占位图冒充有效原意对照。没有找到对应就标明尚未找到，不能写成确认不存在。不同画布或图层分别按真实尺寸展示，不能为凑四列而裁切、拉伸或错配；可用切换视图，不要求四列并排。

审核[来源与语言处理决定](../principles.md)。听译展示实际语音与必要片段定位、工作转写和疑点，文字或图内信息提供可核对来源。真正新增信息明确其语源、用途与采用范围，辅助文案核对功能。原意未确认不能因采用了官方模板而通过；原作已有英文、有理由采用的英文与未解决内容分别说明。

同时展示有意保留的原图／原文及范围、理由和确认依据，与待译、待确认分开。维护者按内容用途、玩家理解和原作表现检查保留是否合理，以及同图应译信息是否已处理；新内容采用同一判断方法，不只检查是否符合既有例子。经确认保留项不能被自动“清除日文”再次改写。保留项的最终绑定也须指向正确原图，而非旧中文候选。

疑问集中展示图片、具体位置、已识读原文、拟定中文、不确定原因与建议。能自行解决的问题先解决；已经认可的保留项和效果不用反复询问。需要“通过／待改”或只收建议的形式按本次送审安排选择，不把界面勾选强加给审核者。

**审核确认的是这一次具体成品。** 保存当前采用版本的路径／摘要与修改意见；返修后更新送审和交付引用，避免已批准新图而打包仍取旧候选。未经确认的生成稿不冒充人工定稿。

每条反馈关联稳定图片编号和本次候选版本，说明如何填写及交回意见；可使用批注、意见文件或页面导出，不强制某种审核界面。页面若只在本机保存意见，明确提示保存／导出并交回，不把本机保存当作已发送。收到意见后核对对应版本再修改，保留已确认结论，避免将旧稿意见套到新图。

同时核对本批的[字体使用记录与声明](../Fonts-ThatFitTheGame/registration.md)：采用图和配方对应，混用字体、继承字层和实际后备字没有漏记；字体换过就更新当前对应，并把旧方案标为历史／已替换。公开来源与致谢随素材更新。仅交付烘焙图片和附带字体软件分别处理；可编辑素材或发布包若含字体文件，保留其适用的完整版权与许可。该项随现有审核与交付完成，不增加一个阶段。

## 引擎交付、实机检查与发布

图片制作经人工确认后，再处理游戏集成；这些交付动作合在最后一个阶段，不另增一套做图步骤。

1. 根据真实脚本、GUI／对象引用验证 01 的中文用途与目标规划，确认语言槽、每个资源 ID、路径和覆盖优先级。中文可覆盖 rUGP 现有 `translation` 槽；底稿和写回目标均不由原意语源推定。不按语言后缀排除，也不自动纳入全部官方差分。不能只凭相似文件名选图；内容相似的 `pattern` 与实际 `chr` 资源可能尺寸、用途不同。
2. 通过对应引擎编码、写回和读回验证，确认画布、透明度、有效区域和游戏缩放。原本应全透明的资源不能因名字像标题就塞入 Logo。
3. 在相关菜单、剧情、日期、状态和差分中实机查看：是否被调用，是否偏移、裁切、闪烁、错语言或出现旧图；新增或采用的呈现是否准确可读，字幕分段和显示／清除时机是否对应语音，是否遮挡正文或操作。动态图层与连续帧还要在实际演出中检查叠放、透明变化、播放时机与连续性。首次集成按作品覆盖范围检查，后续修改重点复查实际受影响位置。
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
Deliver materials that open on the reviewer's actual device: an accessible page
or a self-contained attachment with the required images, explanations and
dependencies. Maintainer-only absolute paths and localhost URLs are not external
review links; check the chosen delivery method, including mobile image loading
when relevant. Existing tools may be supplemented with attachments, instructions
and a separate feedback file; do not claim unsupported tool capabilities.
Show actual layer compositions and playable frame sequences/clips with useful
positions, alongside static detail views. A single layer or selected screenshots
cannot establish approval of the whole dynamic effect.
Verify every actual target, supported geometry/alpha and engine readback;
Chinese may use rUGP's existing `translation` route. In-game checks cover
information, display/clear timing, voice correspondence, obstruction and states.
Check layer order, alpha changes, playback timing and continuity in the actual
sequence too.
The maintainer corrects and verifies issues before publication. Human approval,
integration, in-game verification and release remain distinct facts.
Associate feedback with a stable image ID and the exact candidate version, and
give a simple way to enter and return comments: annotations, a feedback file or
page export as appropriate. If a page stores comments only locally, explain
save/export and return; local saving is not sending. Match incoming feedback to
its version before revising, preserve valid approvals and do not apply old-draft
comments to a different candidate. Do not require a particular review interface.
Organize the review as **official Japanese → official English (if available) →
previous Chinese (if available) → current Chinese**. Keep English accessible even
when used only for comparison. Include the corresponding pre-change Chinese
version where one exists, so reviewers can see both improvements and regressions.
Do not invent counterparts for first-time work or missing official resources.
Label each view's role and version; distinguish released, approved and unapproved
previous Chinese, and identify the exact current review candidate.

Add a short, human-readable explanation beside each image or related group:
where it appears; which text or regions changed; why the wording, layout or repair
was chosen; what was intentionally retained and why; and what still needs human
judgment. Refer to visible positions, explain shared decisions once and individual
exceptions separately. For revisions, explain the previous problem and current
fix; for first-time work, explain the key choices. Filenames, status codes and
execution logs alone are insufficient; reviewers should not need chat history.
Clearly mark candidates awaiting human confirmation. Explanations do not replace
viewing the actual images.

For necessary English-canvas/template
reuse, show the reused part and Chinese output, explain its purpose/reason,
and link Japanese meaning evidence separately. If no same-form Japanese image
exists, show the actual Japanese text, audio or other visual evidence and scene,
and explain which counterpart is missing. A subtitle with a transparent Japanese
placeholder needs its Japanese audio. Distinguish an unfound counterpart from
confirmed absence.
Preserve actual canvas/layer geometry rather than stretching or mismatching
assets to fill a four-column view; switching views is sufficient.
