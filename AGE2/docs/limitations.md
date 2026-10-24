# AGE2 的适用范围与待确认问题

[AGE2 入口](../README.md) · [运行时](../runtime/README.md) · [玩家版本](../../docs/player/README.md)

## 源码和发布包的范围

公开组件支持按稳定身份与日文源摘要连接译文、生成部分图片及构建版本专用运行时。仓库仍缺少重建所有最终图片与字体的全部输入，不能将公开表等同于历史 ZIP 的完整内容。详见[快照与发布兼容性](../evidence/translations/snapshots/compatibility.md)。

自动检查覆盖格式、绑定及被测试的布局条件，不能证明所有剧情、片尾、语音听译、分辨率和语言切换均已人工验收。具体采用与支持范围以相应 Release 为准。[君望 1.0.0「再会」](../games/kiminozo/README.md)的新增／调整文本已完成人工校对；实际运行检查与全路线遍历分开说明。

## 仍需明确适用版本的历史问题

以下事项在原内容记录中没有完整关闭结论，也没有标明每项对应的最终玩家补丁。它们是后续确认的具体范围，不能推广为所有现行版本均有故障。

| 范围 | 尚需确认的内容 |
| --- | --- |
| TDA01 第六次西雅图防卫线四人欢呼字幕的第二句 | 日语末尾的识别结果不可靠，需人工复听；英文图不替代日语听译依据 |
| 帝都 ruby 强调点 | 文本或注音绑定正确不等于强调点的最终视觉效果已确认 |
| 五作完整片尾与字幕演出 | 仍缺全部实际滚动、同显、清除时机和切换方向的覆盖结论 |
| 语言菜单切换瞬间的竖向白条 | 需与原版滚动条行为对照，不与曾经的选中标记遮挡混为一谈 |
| 部分地图的脚本定位 | 原包内存在或制作了候选，不代表已找到所有实际剧情调用 |

已集成的存档摘要、文字缓存和 Log 中文枚举修正见[运行时说明](../runtime/README.md)。TDA 附加字幕的历史字形偏移已有后续候选静态修正，采用与实机范围见[字幕排版](postmortems/caption-layout.md)，不继续将旧候选的偏差写成所有发布版的现状。

## English

The public components do not reproduce every historical release byte for byte. The dated content findings above still need confirmed affected release versions or broader in-game coverage; they are not a claim that every current patch is faulty. Font-cache and save-summary implementations are documented separately from whole-route acceptance.
