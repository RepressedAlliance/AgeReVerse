# 《再诞》身体改造演出文字

`rebirth-text.zh-CN.csv` 保存从原始离线画面核实的英文文字和中文初稿，
包括保密提示、技术标签、部件价格及旁白字幕，共63行。
此文件尚未接入打包器；已制成旁白中文字幕离线预览，完整画面汉化与音画验收仍未完成。

## 版本与帧号

| variant | 带英文字幕 CRsi 全局偏移 | 无旁白字幕 CRsi 全局偏移 | 总造价 |
| --- | --- | --- | --- |
| long | 27493704 | 1715679260 | 900万欧元 |
| short | 117665112 | 1808635048 | 600万欧元 |

脚本链已确认：`short` 出现在前段回忆之后、戈德曼简报之前；
`long` 出现在最终对话和职员表之后。
本任务的结尾制作对象是 `long` 两个资源。短版对照用于区分原片内容、参数和术语，
不能把600万版本当成结尾900万版本的语言变体。

`both` 表示两版都存在且共用该行文字。`long_witness_frame` /
`short_witness_frame` 是对应**英文字幕版本**中人工查看、可辨读的0起始见证帧，
不是入帧点、出帧点或字幕持续时间，也不可直接套用到无旁白字幕版本。
状态 `draft_visual_source_checked` 表示已核实该见证画面的来源文字，
中文仍为初稿。长版22条旁白字幕的连续边界已单独核实；
技术标签逐字动画的覆盖、日语音轨核对仍待完成。
现有本机 ASR 是辅助线索，不是已听校的日语原稿，也不能作为精确时间轴。

`layer` 区分 `notice`、`technical`、`price` 和 `subtitle`。
`body.*` 技术标签在手臂、腿部两处复用，当前见证帧取手臂画面；
实际制作须覆盖两处，不可按CSV行数当作画面出现次数。
眼部标题的“／”用于标记标题与说明两行的排版意图，尚未固定像素布局。

## 旁白字幕离线预览

`rebirth-ending-subtitles.frames.json` 记录长版英文旁白的22个0起始、右端不含帧区间。
逐帧检测后已查看每条的开始前一帧、开始帧、结束前一帧、结束帧。
最后一条在1859帧仅有极弱压缩残影，该帧不计入字幕正文。

原生 CRsi 默认时钟为 `MulDiv(frame, 100000, rate)`，本资源 rate=3000，
对应30fps；播放控制器的覆盖值及音画起点仍未验证。
两条长版视频存在局部帧差，不能把英文字幕版帧号当成无字幕版的精确画面对应。
当前预览只把这些区间按默认时钟转成名义时间，叠加于无旁白字幕版本并配原音轨。

```powershell
python -m rUGP.tools.video.subtitle_track --timeline rUGP/games/photonmelodies/video-localization/rebirth-ending-subtitles.frames.json --text rUGP/games/photonmelodies/video-localization/rebirth-text.zh-CN.csv --output ending-subtitles.ass
```

ASS 时间向下取整到厘秒，以保持30fps各帧时刻的事件归属。已输出本机1904帧预览，
抽查中文排版及首尾边界；技术标签、价格和保密提示仍为原文，未完成音轨听校、
游戏内同步验证或生产 CRsi 编码。该预览不可作为完成的汉化补丁。

## 技术文字布局与清除研究

技术文字的像素区域另见 `rebirth-ending-technical.layout.json`：
25个出现位置覆盖眼部13行、手臂6行、腿部6行；眼部标题拆为两行，
`body.*` 在手臂和腿部分别列出，保密提示不在该文件内。
这些位置只适用于无旁白字幕长版；`detection_span` 是检索窗口，
不是已验收的入出帧。参考帧提取的是字形核心，清除时还须处理抗锯齿和发光边缘。

```powershell
python -m rUGP.tools.video.overlay_masks --video '<原尺寸无字幕长版代理>' --layout rUGP/games/photonmelodies/video-localization/rebirth-ending-technical.layout.json --output-directory '<新的本机私有输出目录>'
```

分析器输出候选显示区间、逐帧强度与字形遮罩。价格包含闪烁，不能简单压成一个
持续显示区间；明亮模型可能影响淡出检测。输出含游戏派生像素，不应提交或公开。
单帧空间修补试片因网格和手腕损伤已否决；时序修复仍在本机评估，未成为生产素材。

## 必须保留的差异

- 长版代号 **Fenice**，短版 **Falso**；长版从死亡与绝望中重生，
  短版曾站在死亡深渊边缘。不能只替换总价与能力数字。
- 长版有 Alternative IV 技术强化句及 G-Code 预约录像功能，短版没有。
- 长版字幕说 reinforced concrete，短版为 concrete；分别译作强化混凝土／混凝土。
- 眼部造价长250万、短200万；手臂长250万、短150万；
  单腿长200万、短125万欧元。两版部件总价分别等于900万、600万欧元。
- 原图出拳数值是2.0／1.5 ton，小数点必须保留；当前按原图单位译作吨，未做单位换算。

## 术语依据

优先沿用 [`translations/再诞.csv`](../translations/再诞.csv) 的
西尔维奥·奥兰迪、欧盟情报军中尉、菲尼切、超陶瓷、多用途光学传感器，
以及“电磁伸缩碳带”的旁注“碳素驱动器”。
Cybrid 沿用现有译文的拉丁名称；Alternative IV 对齐现有写法 Alternative 4。
Falso 对应ファルソ，按
[`terminology/baseline.ja-zh-Hans.csv`](../terminology/baseline.ja-zh-Hans.csv)
的审定条目及戈德曼简报正文使用“伪面”，替换初稿临时音译。

详细格式、证据及未完成的读取链路见
[`crsi-rebirth.md`](../../../docs/crsi-rebirth.md)。
