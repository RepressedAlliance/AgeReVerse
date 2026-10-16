# CRsi 离线工具入口

在仓库根目录运行下列命令。只处理自己合法持有的本地资源；仓库不附游戏 EXE、
RIO、CRsi、音轨、代理视频或字体。算法和容器原理见[规格](../../docs/crsi-format.md)，
C 的构建、ABI 和验证入口见[核心说明](../../formats/video/README.md)。
当前制作结果及素材配置见[《再诞》说明](../../games/photonmelodies/video-localization/README.md)
和[回顾标题／倒计时说明](../../docs/story-video-labels.md)，完整内容范围见
[PM／PF 视频资源普查](../../docs/photon-video-scope.md)。

## 按用途准备依赖

| 用途 | 依赖 |
| --- | --- |
| 对象提取、Python 容器测试 | Python 3.10+ 标准库 |
| C 检查／指定帧 BGRX 导出 | C 编译器及标准库；实际验证 Windows x64 / Zig 0.16.0 |
| 全片无损代理导出 | Python、明确构建的 C 库、FFmpeg（FFV1 编码） |
| 视频比较和替换编码 | NumPy、OpenCV；显式 `--codec-library` 使用 C；省略时需要 Numba |
| ASS 字幕生成 | Python 标准库；烧录预览另需带 libass 的 FFmpeg 与相应字体 |
| 图字遮罩、修补合成、样式和旁白制作 | NumPy、OpenCV、Pillow、fonttools；合成器另需 FFmpeg 与合法字体 |
| 原版离线 oracle | pefile、Unicorn、Pillow；合法且 SHA 锁定的 PM EXE |

`requirements.txt` 是这些可选制作／研究依赖的集合，不能当作 C 工具的运行要求。
现有测试环境主要为 Python 3.12；未在每个最低依赖版本上逐一验证。
复用已有环境，需独立环境时可在自己的虚拟环境执行
`python -m pip install -r rUGP/tools/video/requirements.txt`。FFmpeg 和编译器单独准备。

## 从归档到可编辑的完整影片

先用[RIO 清点工具](../catalog/rio_inventory.py)及资源目录确认对象所属卷、
**卷内字节偏移**和完整 extent。全局地址不能直接用于 `.003` 等卷。
目录中的顶层 CRsi 数量不等于内嵌对象总数；本工具不扫描魔数猜测身份。
以下以已核实长版 Translation 对象为例（卷内偏移 27493704、长度 90171399）：

```powershell
python -m rUGP.tools.video.crsi_workflow extract '<photonmelodies11.rio>' 27493704 90171399 '<source.crsi>'
& '<crsi_tool.exe>' inspect '<source.crsi>'
python -m rUGP.tools.video.crsi_workflow export '<crsi_codec.dll>' '<source.crsi>' '<source.mkv>' '<export.json>' --ffmpeg '<ffmpeg.exe>'
```

`extract` 验证完整容器闭合后排他创建文件，单对象最大 1 GiB，偏移／大小可用十进制或 `0x`。
`export` 顺序解码所有帧，保留预测状态，以 `rate/100` 写入原尺寸、无音轨 FFV1 MKV。
RGB 逐像素无损；原生 X 字节仅保存在逐帧 BGRX 哈希中，不解释为透明度。
源对象保存在内存，像素流逐帧送入 FFmpeg；代理可能很大，应预留空间。
报告记录源 SHA、每帧 RGB／BGRX SHA、覆盖帧数。它证明 C 解码与代理写入完成，
不证明与原版解码一致、完整观看或音画同步。失败报告标记 `incomplete`，失败代理
可能只有前段帧，不能继续作为生产输入；另选新路径重试，工具不覆盖已有结果。
没有隐藏 native fallback；未支持的模式或坏帧直接报帧号。
PM 总 OP（卷内1341451580）1073依赖帧曾触发 C 码本范围拒绝；现已依据原生
相邻表的确定值修复，并核对1069–1076八帧。其他未观察越界仍拒绝，不能声称列出的
0x0575/8 所有源流均支持。详见[规格中的具体边界](../../docs/crsi-format.md)。
跨 PM/PF 的43个 CRsi 清点和画面审核是资源范围，不能代替全帧原生交叉验证。

用 FFmpeg／ffprobe 检查代理帧数、尺寸、帧率；制作器也会拒绝尺寸、帧率和帧数改变。
需要独立原生一致性证据时，在编辑前执行：

```powershell
python -m rUGP.tools.video.verify_portable '<crsi_codec.dll>' '<source.crsi>' '<native-source.json>' --executable '<PM EXE>'
```

完整原生回放会较慢。`--profile-samples` 是明确标记的抽样选项，不能称作全帧原生验证。
`export.json` 使用顶向下哈希，**不能**直接传作 `verify_portable --baseline`：后者
仅接受旧 `decode.json` 的底向上完整 BGRX 基准。见核心说明。

## 制作并验证候选 CRsi

保留完整 `source.mkv`，另生成同尺寸、同帧率、同帧数的 RGB 无损 `edited.mkv`。
不要用 MP4/H.264 预览充当无损生产输入。旁白制作器按共享样式、字体和明确帧区间
处理；两个演出分别使用自己的版本配置，不能靠统一帧偏移互换。

```powershell
python -m rUGP.tools.video.caption_compositor '<source.mkv>' '<background.mkv>' '<timeline.json>' '<text.csv>' '<style.json>' '<font.ttf>' '<edited.mkv>' '<composition.json>'
python -m rUGP.tools.video.encode_replacement '<source.crsi>' '<source.mkv>' '<edited.mkv>' '<candidate.crsi>' '<build.json>' --codec-library '<crsi_codec.dll>'
python -m rUGP.tools.video.verify_portable '<crsi_codec.dll>' '<candidate.crsi>' '<c-target.json>' --target-build '<build.json>'
python -m rUGP.tools.video.verify_replacement '<PM EXE>' '<candidate.crsi>' '<build.json>' '<native-target.json>'
```

替换器比较源／编辑 RGB，只把改变帧及直到下一个原独立帧前的依赖闭合帧写成
独立 0x03ff 无损帧；其余载荷保留原字节。C 生产路径不导入 Numba。
`--target-build` 检查 C 还原是否符合目标 RGB；`verify_replacement` 另外用锁定 EXE
逐帧核对目标 RGB 和原生帧表。已验证完全相同基准的复用选项见其 `--help`。
成功编码和原生 RGB 一致仍需连续视觉审阅和限定游戏验收。
当前工作只生成、验证候选对象；正式补丁接入另按项目计划执行。

## 完整对象的 RUO 封包入口

已有封包器接受完整 CRsi（含父头、全部索引和载荷），不是只接收改变帧或 MKV。
以下示例在已验证候选之外创建一个新累积 RUO，保留既有映射：

```powershell
python -m rUGP.formats.rio.ruo --unit-size 4 --source-byte-offset 27493704 --record '<candidate.crsi>' --base-ruo '<现有汉化.ruo1>' --output '<新的累积.ruo1>' --manifest '<新的封包报告.json>'
```

这里 source-byte-offset 是原对象的**全局字节地址**，与提取时的卷内偏移概念不同；
示例位于主卷，二者数值恰好相等。多个对象可用 `build_ruo()` API 一次传入完整替换表，
或逐次 CLI：下一步明确把上一步输出传入 `--base-ruo`，每次用新输出和报告路径。
不要把分别基于同一旧 RUO 生成的几个独立结果叠加安装，否则后者可能丢失前者映射。
实际五资源整合、路由闭合及未来验收顺序见
[补丁接入规划](../../packaging/video-integration-plan.md)；本指南的命令示例不等于已制作或发布最终补丁。

## 制作与逆向工具索引

| 模块 | 用途与边界 |
| --- | --- |
| `subtitle_track` | CSV + 明确时间轴 → ASS；校验 ID、重叠和控制字符 |
| `overlay_masks` / `technical_track` | 固定技术字形分析及 ASS；检测阈值不是验收时间轴 |
| `notice_background` | 开场提示背景估计；属于特定素材制作方法 |
| `caption_compositor` | 相邻无字画面背景与中文旁白合成；报告允许区域之外的改动 |
| `story_labels` | PM 回顾标题与 PF 倒计时的专项排字；固定资源尺寸、帧数和可变字体，不是通用去字工具 |
| `compose_repairs` | 按修补报告组合裁块，检查遮罩外像素；不包含 ProPainter 模型 |
| `style_layers` | 共享样式字体渲染库；没有 CLI |
| `portable_codec` | 明确 C 库的 ctypes API；没有 CLI、隐式编译或自动回退 |
| `compact_encoder` | 可选 NumPy/Numba 0x03ff 无损实现；兼容参照，C 是当前生产选择 |
| `native_crsi` | 版本锁定原版叶函数 oracle API；没有 CLI，不是全引擎播放器 |
| `native_crsi_table` | 原父头／帧行反序列化核对；archive 与分配为模拟对象 |
| `native_ruo` | 原生重定向地址／长度核对；不执行实际文件线程和游戏播放 |

有 CLI 的模块均可用 `python -m rUGP.tools.video.<模块> --help` 查询输入。
原生反序列化与地址核对示例：

```powershell
python -m rUGP.tools.video.native_crsi_table --executable '<PM EXE>' '<source.crsi>' '<candidate.crsi>'
python -m rUGP.tools.video.native_ruo --executable '<PM EXE>' --ruo '<候选 RUO>' --source-key '<原对象键>' --original-size '<原对象完整字节数>'
```

`native_ruo` 的默认 456 字节是合成见证值；真实资源验证必须传实际长度。
原生 oracle 的 EXE SHA、内存／指令限制在源码明确列出；其他游戏或版本不自动接受。
0x016d 仅有研究 oracle 路径，C 生产工具不宣称支持。0x0575 有损 writer 仍属研究，
不能用压缩率或“原生可解”替代字幕画质验收，也不用于以上生产命令。

## 可公开的检查

```powershell
$env:RUGP_CRSI_LIBRARY = (Resolve-Path '<crsi_codec.dll>').Path
python -m unittest discover -s rUGP/tests/formats/video -t . -v
```

不需要游戏素材；C 和 FFmpeg 集成测试在依赖未显式提供时会跳过，须检查实际输出。
全片导出测试用两帧黑白合成序列，并重新解码 FFV1 比较全部 RGB，另检查范围拒绝、
不覆盖与失败报告。真实素材覆盖和限制见[验证证据](../../evidence/photon/video/crsi-tools-workflow-20261012.json)。
