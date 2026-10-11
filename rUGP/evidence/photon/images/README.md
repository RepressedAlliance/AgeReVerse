# Photon 图片资产：找到素材、来源与制作入口

[Photon 数据](../README.md) · [资产地图](../../../../docs/research/asset-map.md) · [图片制作](../../../../Localization-MakeGamesSpeak/Images-MakeItLookNative/README.md)

Git 保存资源清单、语言对应、制作状态和工具输入描述。图片包位于独立研究 Release，不是玩家安装包；玩家下载从[玩家指南](../../../../docs/player/README.md)进入。

> **历史研究资产仍待分发整改：**V6 中有 19 张 PNG 与官方来源文件字节相同，下一份可分发资产应移除这些文件或改由合法本机输入重建。技术身份正确不代表已取得分发许可，参见[资产与发布政策](../../../../docs/project/asset-and-release-policy.md)。

## 选择对应的目录

| 内容 | 入口 |
| --- | --- |
| 静态图的分类、官图配对和制作状态 | [1,791 项静态图目录](static-review-20260909/README.md) |
| V6 的 1,490 项图片身份 | [manifest.json](manifest.json)：资源 ID、尺寸、源／候选／PNG／RGBA 摘要与原生记录 |
| CRmt 演出与全部内嵌层 | [CRmt 目录](../crmt/README.md)与[家族指南](../../../docs/crmt-family.md) |
| 日英及共享资源的逻辑端点 | [路线目录](../routes/README.md) |
| 文字、字体、配方与最终采用 | [制作规范](../../../../Localization-MakeGamesSpeak/Images-MakeItLookNative/production.md)与[图片字体](../../../../Localization-MakeGamesSpeak/Fonts-ThatFitTheGame/images.md) |

## 使用历史 V6 图片包

- [Release 与附件](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/photon-images-1490-20260824-v6)
- [图片 ZIP](https://github.com/RepressedAlliance/AgeReVerse/releases/download/photon-images-1490-20260824-v6/MuvLuv_Photon_PF_PM_CN_Images_1490_20260824_v6.zip)
- [包内内容与限制](release-notes.md)

其中 243 项以封存的原生记录为打包依据，PNG 是双解码得到的预览；不要将这些预览重新编码后冒充原记录。审阅 JPG 也不作为打包输入。

仓库 `manifest.json`／`verification.json` 对应 Release 的 `manifest-v6.json`／`verification-v6.json`。仓库 [SHA256SUMS.txt](SHA256SUMS.txt) 使用附件名；ZIP 附带的校验文件检查整个 ZIP，ZIP 内部的同名清单检查成员，三者用途不同。

## 西瓜教程整帧与动态计时器

[教程路线表](pm-watermelon-timer-runtime-routes-20260904.json) 区分 11 个动态计时器、12 个逻辑整帧与 11 个唯一整帧载荷。计时器与整帧不是同一资源，两个逻辑帧可以共用物理载荷。零秒圈线、文字遮挡与图片语言选择的方法见[运行时案例](../../../docs/postmortems/image-transport-runtime.md)。这些增补不改写 V6 的历史范围，也不表示它们已包含在 V6 ZIP 中。

## English

Use these catalogs to find image identities, official locale pairs, authoring decisions and build inputs. The historical V6 ZIP is research material with an outstanding redistribution issue, not a player installer. Native-authority previews, runtime sidecars and logical image routes are distinct assets.
