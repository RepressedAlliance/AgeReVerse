# Photon 本地化数据入口

[rUGP](../../README.md) · [PF](../../games/photonflowers/README.md) · [PM](../../games/photonmelodies/README.md)

| 需要什么 | 入口与用途 |
| --- | --- |
| 修改现行中文 | [章节 CSV](../../docs/chapter-texts.md)：PF 13,025 条、PM 44,698 条，正文与批注的维护入口 |
| 比较早期译文 | [reviewed](text/reviewed/README.md)：57,547 行历史基线，保留稳定身份与源摘要 |
| 精确 CString 写入合同 | `text/runtime/manifest.json`：PF 69 行、PM 151 行，记录容量与控制约定 |
| 静态图与制作状态 | [images](images/README.md)：V6 历史资产与后续选集分别维护 |
| 演出图与缩放层 | [crmt](crmt/README.md)：父对象、语言配对、各层及处理决定 |
| 图片的逻辑语言端点 | [routes](routes/README.md)：1,448 个 translation peer 与 42 个 shared/common 端点 |

`text-data/layout-baseline` 保存不可变绑定基线，当前正文只在章节 CSV 编辑；回归数据与历史合同不是第二套新正文。完整官方日英脚本由使用者从合法游戏副本提取，不在此镜像。

这些数据有不同版本与计数单位。译文被审阅、记录可写、图片来源明确、逻辑端点正确和实际显示正常各自说明不同事项，不能互相替代。具体格式与适用范围见各目录说明，整体限制见[Photon 适用范围](../../docs/limitations.md)。
