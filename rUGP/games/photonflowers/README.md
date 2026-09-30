# 光子之花（PF）Steam 简体中文汉化补丁

Muv-Luv photonflowers*／マブラヴ photonflowers*。AgeReVerse · 压抑同盟作品项目。

[返回 rUGP 游戏](../README.md) · [项目清单](project.toml) · [文本](translations/) · [图片](images/) · [完整工作流](../../../localization/workflow.md)

- Steam App ID：`889700`
- 目标语言：简体中文（`zh-Hans`）
- 玩家包：已发布 [BETA 0.1.2](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/pf-BETA-0.1.2)
- 最新章节编辑表：13,025 条（包含系统文本与补提取消息）
- 历史已审校文本：Alternative 6,033 行、Extra 6,931 行，共 12,964 行
- 当前精确运行时绑定表：69 行
- Photon 图片权威：光子之花 636 项

## 玩家实机预览

本作汉化范围覆盖正文、菜单、设置、故事介绍和各类图片文字，包括年表、手绘地图与机械说明图。
[查看七张中文实机截图](../../../docs/player/screenshots.md#光子之花pfrugp)。补丁仍为 BETA，部分页面偶发英文尚待修正，后续会继续补齐。

[按章节命名的 CSV](translations/README.md) 是最新人工编辑入口。
`text-data/history/reviewed/` 保留早期审校中文、稳定 ID 和日文源哈希，作为封存证据，不再人工编辑。
`text-data/runtime/zh-Hans.csv` 保存偏移、容量、控制符、运行时值和写入路线，仍是原有 69 行
写入合同。章节 CSV 读取接口不会把全部审校文本自动变成可安全写回的原生字段。

公开表故意不批量镜像完整官方日文。贡献者从合法游戏提取源文本后，通过稳定 ID 与
源哈希连接。图片使用光子之花/光子旋律共用的 [Photon 清单](../../evidence/photon/README.md)，但
光子之花有自己的输入哈希、运行时配置、安装包和实机 QA；光子旋律的成功不能替代光子之花。

玩家请使用上面的 BETA 0.1.2 安装包；源码树和 1,490 图研究资产 Release 不是玩家安装包。
安装、恢复及已知问题见[玩家指南](../../../docs/player/README.md)。当前发布不代表全路线已人工遍历；后续构建仍需独立验证。

## 校对与致谢

感谢 **柚子コショウ** 参与本作校对、提出用词与称呼问题并提供修正建议；详见[BETA 0.1.2 更新记录](../../../docs/project/photon-beta012-proofreading.md)。
感谢 **红桃皇后假说** 为《樱花盛开之前》提供部分文本。
项目维护、技术参考与其他贡献见[贡献者总表](../../../docs/project/CONTRIBUTORS.md)。

## English summary

光子之花 has 13,025 latest review entries in chapter CSVs, a sealed legacy
12,964-row review dataset, 69 existing runtime contracts and 636 image authorities.
The chapter editing surface is not a player package or a native write contract.
