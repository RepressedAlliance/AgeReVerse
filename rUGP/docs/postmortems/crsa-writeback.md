# CRsa 写回：字段正确之外，还要选择正确的存储路线

[原生字段](crsa-fields.md) · [CString 的 8311 错误](error-8311.md) · [RUO](ruo-overlay.md)

## 先绑定现行字段，再写入

`crsa_vm_edit.py` 以目标记录的明文、命令、索引及正文／批注摘要确认身份。写正文保留原有池索引；修复日文批注索引不改日文文本字节。正文、批注键与批注内容共同决定显示，不能只补一个看起来正确的字符串。

正文已经表达含义、或批注只有日语读音时，不必另插中文解释。有额外信息的批注才译入；键须能在当前正文中唯一匹配。例如长德语从句改写后，可选 `bitte` 等实际存在的短锚点，不能沿用已经不存在的整句键。

默认不增长字符串池。额外空间只能来自已证明未引用的空闲连续槽，或明确锁定索引、摘要与容量的旧残留；追加必须有对应 manifest 的存储授权。旧布局快照和增量契约不能直接覆盖后来修正过的措辞、换行或批注。

写后重新解析，比较所有非目标池字节、命令、计数字符串、音声引用、对象后缀及覆盖路由。源绑定漂移应停止构建，不以放宽摘要检查继续。

## 光子之花与光子旋律不能共用一种覆盖方案

光子之花使用一份累积 RUO，保留已有路由并合入获准增量。光子旋律后分卷的 CRsa 曾在**内容不变的重编码重定向**中出现 `InternalError(831)`，同一记录放回原固定范围则通过。因此这个 831 案例属于传输路径问题，与[计数字符串内 NUL 导致的 8311](error-8311.md)分开。

光子旋律原生文本采用干净分卷的新副本及固定物理长度写入，配合版本／摘要限定的段补丁。构建器拒绝覆盖输入、沿用未知 RUO、增长记录、区间重叠及修改非目标字节。不要为了统一文件形式，重新把后分卷正文放进独立 RUO。

下面复用仓库中的历史增量契约演示两种构建入口；它们不是将旧增量直接叠加到任意新发布包的命令：

```powershell
python -m rUGP.tools.text.build_crsa_native_volume_patch --spec rUGP/games/photonmelodies/text-data/increments/crsa-native-20260904.json --source-dir "<clean PM game directory>" --output-dir "<new work directory>/pm-native-fixed-volumes"
python -m rUGP.tools.text.build_crsa_native_increment --spec rUGP/games/photonflowers/text-data/increments/crsa-native-20260904.json --source-dir "<PF game directory>" --base-ruo "<PF game directory>/photonflowers11.rio.ruo1" --output "<new work directory>/pf-native.ruo"
```

## 字体与运行时一起交付

补入新译词后重新计算正文与批注的字形覆盖。缺字增补使用获许可的源字体，保留基底的旧字形、度量和映射，见[字体工具](../../../Localization-MakeGamesSpeak/Tools-LetToolsHandleRepetition/README.md)。`rebind_photon_font.py` 仅更换运行时内锁定的字体摘要；新字体必须与对应 DLL 成套交付，并附来源和许可。

解析回读不能证明所有提示、批注键、小游戏与旧存档都正常。实机应覆盖新增字段所在的实际界面；语音识别结果仍需人工听辨，不将自动识别或抽样显示解释为全路线人工校对。

## English

Bind edits to the effective plaintext and native references. Reuse only proven free storage; pool growth needs an explicit contract. PF merges into one cumulative RUO. PM later-volume native CRsa uses fixed-extent volume staging after an unchanged redirect reproduced error 831. Keep this transport failure separate from counted-CString error 8311, and ship font changes with their matching guarded runtime.
