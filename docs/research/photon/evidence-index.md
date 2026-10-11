# Photon 组件与资产索引

[总览](README.md) · [技术来源](provenance.md) · [技术蓝图](blueprint.md)

从要复用的组件进入源码、数据和使用说明。历史发布件按自己的版本识别，不把早期文件摘要当作现行安装状态。

| 内容 | 入口 |
| --- | --- |
| 目录读取与加密 | [catalog 工具](../../../rUGP/tools/catalog/README.md)、[RIO 格式](../../../rUGP/formats/rio/README.md) |
| 正文、批注与稳定绑定 | [章节表](../../../rUGP/docs/chapter-texts.md)、[原生字段](../../../rUGP/docs/postmortems/crsa-fields.md)、[写回路线](../../../rUGP/docs/postmortems/crsa-writeback.md) |
| 像素编解码 | [图像格式](../../../rUGP/formats/images/README.md)、[CRmt 家族](../../../rUGP/docs/crmt-family.md) |
| 图片来源和语言端点 | [图片目录](../../../rUGP/evidence/photon/images/README.md)、[路线目录](../../../rUGP/evidence/photon/routes/README.md) |
| 私有字体与运行时 | [字体来源](../../../Localization-MakeGamesSpeak/Fonts-ThatFitTheGame/README.md)、[运行时构建](../../../rUGP/runtime/README.md) |
| 差分与玩家安装器 | [打包](../../../rUGP/packaging/README.md)、[玩家指南](../../player/README.md) |
| 旧版组件身份 | [shipped-fixed-files.json](evidence/shipped-fixed-files.json)：PF BETA 0.1／PM BETA 0.1.1 的固定文件，供指定旧版比较 |
| 已知限制与具体故障 | [适用范围](../../../rUGP/docs/limitations.md)、[案例索引](../../../rUGP/docs/postmortems/README.md) |

代码、源身份和公开样本描述可供继续研究。运行工具仍需要匹配的合法游戏输入；MIT 代码许可不授予官方素材分发权，参见[第三方说明](../../legal/THIRD_PARTY.md)。
