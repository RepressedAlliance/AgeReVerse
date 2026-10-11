# 帝都燃烧原版资源布局

[本作入口](../README.md) · [字幕排版](../../../docs/postmortems/caption-layout.md)

以下数据对应所列 `pack.bin` 指纹，用于选择解析器与定位资源。其他 Steam 版本应重新读取索引。

## 原版定位与指纹

- appmanifest：Steam 库内 `steamapps/appmanifest_2630300.acf`
- 安装目录：由该 appmanifest 的 `installdir` 与当前 Steam 库根目录解析；不绑定制作者盘符
- 资源包：`obb/pack.bin`
- 大小：965,436,479 bytes
- SHA-256：`1D749713C01AE4E825A82FA2E75BF232303B1510708BBC9B7B98275315F7344F`
- 容器：FPD v2；42,588 项；数据起点 `0x178214`

## 扩展名统计

| 扩展名 | 数量 | 包内存储字节 | 判断 |
|---|---:|---:|---|
| `.webp` | 18,705 | 255,750,877 | GUI、角色/事件图片、文字条等 |
| `.xml` | 11,226 | 3,941,606 | 索引、脚本旁挂信息及资源描述 |
| `.fcd` | 4,366 | 359,061,509 | FSNr 加密媒体，包含 JP 语音等 |
| `.txb` | 3,300 | 0 | 与 `.zstd` 成对的纹理描述 |
| `.zstd` | 3,300 | 70,295,160 | 压缩纹理数据 |
| `.avif` | 1,175 | 48,823,868 | 图像资源 |
| `.pso` | 218 | 649,412 | 着色器 |
| `.gut` | 168 | 610,283 | GUI/布局相关容器 |
| `.egpack` | 74 | 5,520,628 | ADV 多语言文本表 |
| `.ogv` | 22 | 195,796,540 | 过场视频；抽查的帝都燃烧篇 avant 为无音轨画面 |
| `.epk` | 8 | 61,954 | FSNr 文本/配置容器，包括 `uistring.epk` |
| `.png` | 7 | 58,600 | 图像 |
| `.json` | 7 | 12,524 | 配置/描述 |
| `.vso` | 6 | 11,628 | 着色器 |
| `.otf` | 4 | 23,299,432 | 字体 |
| `.cfg` | 2 | 1,830 | 字体配置 |

主要分布：`root/assets/data_spec/adv/game` 40,924 项；`data_spec/gui/textures` 564 项；`data/gui/textures` 449 项；`data/adv/sys` 227 项。数值来自修正后的 FPD v2 索引解析，不以相邻作品结构代替本作证据。

## 引擎与工具路线

- 外层为 FPD v2，使用 [`../../../tools/fpd/`](../../../tools/fpd/) 与对应 `Scrambler.cs` 只读解析/筛选提取。
- 正文表为 EGPACK，使用 [`../../../tools/egpack/`](../../../tools/egpack/)。
- `uistring.epk` 使用 FSNr EPK 工具解密/加密；补丁器仅改可见字段，并强制精确 JP baseline。
- `.fcd` 使用 FSNr FCD 解密获得 JP OGG，供文字条听译核对；不改写语音。
- `.webp` 可直接作为 loose overlay；文字条可用 Pillow 与本作选定字体制作 lossless WebP，具体配方见图片与字体说明。
- 本作未发现需要走 RIO/CRsa 的目标；旧 rUGP 经验仅用于排除格式，不进入 AGE2 工具链。


零字节影片索引需与同名纹理数据一起判断。字体、日期地点卡和地图是否处理，按当前项目与具体素材决定，不以早期阶段清单作为永久排除规则。
