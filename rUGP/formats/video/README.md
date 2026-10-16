# CRsi C 核心与制作工具

原理、位流和边界见[CRsi 规格](../../docs/crsi-format.md)。这些是离线工具；
玩家继续使用原版引擎解码 RUO 中的资源，不安装 Python 或此工具 DLL。
从 RIO 完整提取、全片无损导出、编辑、编码及独立验证的串联命令见
[视频工具工作流](../../tools/video/README.md)。

## 构建

依赖仅为 C 标准库。以下在仓库根目录执行，`zig` 使用已有编译器路径即可。
产物写到已忽略的任务目录，不与游戏 DLL 混用。
先创建自己的产物目录（示例目录不存在时运行 `New-Item -ItemType Directory
-Path 'local-internal/pm-rebirth-video'`）。输出库路径由调用方显式提供。

```powershell
zig cc -shared -O2 -ffp-contract=off -Wall -Wextra -Werror rUGP/formats/video/crsi_codec.c rUGP/formats/video/crsi_lossless.c rUGP/formats/video/crsi_container.c -o local-internal/pm-rebirth-video/crsi_codec.dll
zig cc -O2 -ffp-contract=off -Wall -Wextra -Werror -municode rUGP/tools/video/crsi_tool.c rUGP/formats/video/crsi_codec.c rUGP/formats/video/crsi_lossless.c rUGP/formats/video/crsi_container.c -o local-internal/pm-rebirth-video/crsi_tool.exe
```

Windows CLI 使用宽字符路径。源码保留非 Windows `main`；本轮实际构建与执行为 Windows x64，
不声称已测试其他平台。其他平台通常需要共享库相应选项和数学库，不使用 `-municode`。
禁止 `-ffast-math`；码本生成要保持原版浮点求值顺序。

## 独立命令行

```powershell
& local-internal/pm-rebirth-video/crsi_tool.exe inspect '<完整 CRsi>'
& local-internal/pm-rebirth-video/crsi_tool.exe decode '<完整 CRsi>' 1140 '<新文件.bgrx>'
```

`inspect` 验证完整容器并报告尺寸、帧数、rate 和配置统计。
`decode` 从目标帧之前最近的独立帧恢复依赖，导出顶向下的原生 BGRX；
X 不作透明度解释，导出路径必须不存在。支持四种已观察 codec-1 与不透明 0x03ff。
文件读取器目前限制单个对象不超过 1 GiB；库接口与 CLI 的限制分别在头文件和源码列出。

## 接入现有制作流程

`crsi_codec.h` 提供解码、不透明无损编码以及研究用有损编码接口。
后者的 `reconstructed` 是下一依赖帧应使用的实际反馈表面。
尺寸、容量和配置错误会拒绝；解码失败后的输出可能已部分写入，调用方必须丢弃。
`crsi_container.h` 提供借用输入内存的帧视图及完整帧计划写回；输入缓冲区须保持有效。

已有视频制作器可显式选择 C 编码，不再导入 Numba：

```powershell
python -m rUGP.tools.video.encode_replacement '<原 CRsi>' '<原 FFV1>' '<中文 FFV1>' '<新 CRsi>' '<新报告.json>' --codec-library '<crsi_codec.dll>'
```

该路径仍只写 0x03ff 无损独立替换帧，保留原有依赖闭合逻辑；不会暗中改用有损编码。
C 后端不统计各像素操作数量，报告的 `statistics` 为 null，`encoder_backend` 为 `portable-c`。
原生验证和视觉制作要求不变。

## 验证

```powershell
$env:RUGP_CRSI_LIBRARY = (Resolve-Path 'local-internal/pm-rebirth-video/crsi_codec.dll').Path
python -m unittest rUGP.tests.formats.video.test_portable_codec -v
python -m rUGP.tools.video.verify_portable '<crsi_codec.dll>' '<原 CRsi>' '<新报告.json>' --baseline '<此前完整原生 decode.json>'
python -m rUGP.tools.video.verify_portable '<crsi_codec.dll>' '<中文 CRsi>' '<新报告.json>' --target-build '<制作报告.json>'
python -m rUGP.tools.video.verify_portable '<crsi_codec.dll>' '<RIO卷>' '<新报告.json>' --offset 219563360 --size 598632633 --executable '<合法 PM EXE>' --profile-samples
```

保存的基准绑定完整对象 SHA，逐帧比较包含 X 的原生 BGRX；只有既有基准文件采用
底向上字节顺序时才能使用该入口。传入原版 EXE 时执行独立的版本锁定离线原生 oracle。
`--target-build` 核对制作报告中的目标 RGB，不把仅与制作输入一致计为新的原生验证。
`--profile-samples` 包含每个非 0x0575 帧及后继、均匀选择的帧，并追溯各自独立帧，
确保不是给原生解码器随意拼接预测状态。小于 400 帧的对象在该模式下完整比较。
默认不抽样。未传基准或 EXE 时只验证 C 能完成解码，报告不会计为原生一致。

验证不启动游戏、不读取存档。没有图像和音轨素材随源码发布。
