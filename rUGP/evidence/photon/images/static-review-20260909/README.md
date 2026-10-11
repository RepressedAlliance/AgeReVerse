# Photon 静态图目录：分类、语言来源与制作状态

[图片总入口](../README.md) · [制作流程](../../../../../Localization-MakeGamesSpeak/Images-MakeItLookNative/README.md)

`catalog.json` 保存 1,791 个登记项，其中 1,789 项含图片身份、2 项仅有状态。它是特定选集，不是全部解包资源或最终安装包的成员表。

| 分类 | 项数 |
| --- | ---: |
| 章节与标题 | 110 |
| 设置与角色 | 624 |
| 存档与读档 | 164 |
| 游戏内操作 | 164 |
| 鉴赏与附录 | 126 |
| 小游戏与地图 | 149 |
| 地图与剧情资料 | 86 |
| 剧情图片 | 360 |
| 制作与片尾 | 8 |

## 如何读取条目

- `official.jp`／`official.en` 表示已确认的官方语言对应；`shared_native` 表示已确认共用画面；`unknown` 保留语言未确认的来源。缺少配对项不证明另一语言不存在。
- `refs` 记录分卷与资源位置，`source_resource_catalog_sha256` 绑定资源目录；图片 `sha256`／`size` 绑定对应成图，不能直接替代运行时 payload FNV。
- 制作登记、候选图、安装采用和实际显示分别记录。历史选集中的 `candidate` 不自动表示当前仍未发布，最终采用以相应包清单为准。
- 角色卡有 18 人的无圈／白圈／黄圈，以及彩峰、柏木、纯夏、霞四个暗态，共 58 态。见[状态矩阵](oval-state-matrix.json)，不为其他角色臆造暗态；解锁条件另查。

## 从本地输入生成审阅页

先用 [export_static_review.py](../../../../tools/provenance/export_static_review.py) 投影资源身份，再用 [build_static_review.py](../../../../tools/images/build_static_review.py) 和显式资产映射生成分类页与长 PNG。摘要、尺寸或共用像素不符会拒绝生成；缩略概览仍需配合原尺寸画面。

## 供工具使用的数据

| 数据 | 用途 |
| --- | --- |
| [catalog.json](catalog.json)、[oval-state-matrix.json](oval-state-matrix.json) | 图片来源、分类及已存在的角色卡状态 |
| [pending-script-routes.json](pending-script-routes.json)、[runtime-pending-groups.json](runtime-pending-groups.json) | 未观察调用的精确身份、脚本关系与定位分组，见[场景入口](../../../../docs/postmortems/pending-hook-entry-points-20260909.md) |
| [cr6ti-replay.json](cr6ti-replay.json)、[crip008-replay.json](crip008-replay.json)、[native-sites-offline.json](native-sites-offline.json) | 事务及调用点回归样本描述，配合[运行时检查方法](../../../../docs/postmortems/runtime-validation.md) |
| [runtime-sync.json](runtime-sync.json) 与 `*.build.json` | 该快照对应的表、配置及输出身份，不是“当前玩家已安装文件”的动态查询 |

默认构建与显式姓名颜色配置的 manifest 分开保存；PM 表还含按编译游戏选择的不同视图。不能将同一目录里修改时间较新的所有文件直接拼成另一作的构建输入。可用选项见[运行时](../../../../runtime/README.md)。

## English

This dated catalog separates image origin, authoring state, runtime identity and package adoption. Language slots describe official ownership, not the language visible in the pixels. Use the tools with locally supplied assets; build manifests and regression data describe their fixed snapshot, not a live installation.
