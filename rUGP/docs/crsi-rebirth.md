# 《光子旋律·再诞》结尾 CRsi 演出研究

状态：第一阶段进行中（2026-10-10）。已完成连续离线解码和替代帧编码探针；
**尚未完成游戏播放替换验证，没有中文成品，不可作为玩家交付。**

## 三个研究方向及适用边界

| 来源 | 版本／证据 | 可复用之处与缺口 |
| --- | --- | --- |
| [GARbro](https://github.com/morkt/GARbro/blob/b09ee4570ccb1daf6ac56710ee8934dc0b8baeb0/ArcFormats/rUGP/ArcRIO.cs) | 项目现行目录读取器的固定上游 | ICI/RIO 对象身份、偏移、长度；不是本演出的完整重封装器。 |
| [rugptools](https://github.com/osmium76/rugptools/tree/3ff587416e41eeeee7122fb122c90f7a36c409dd) | README 限定初版 MLA DVD；借鉴 hiko_bae alterdec | 对象与图片研究背景，不能直接推广到 PM Steam。 |
| [muzhi 的 RioX 发布及研究帖](https://xycq.org.cn/forum/viewthread.php?action=printable&tid=247211) | 作者一手记录，最后编辑 2013-10-08 | 说明 alterdec、RioX、Hook 的来源与限制；旧帖提及音视频插件线索，不证明当前无人研究视频。 |
| [Steam 玩家讨论](https://steamcommunity.com/app/449830/discussions/0/133258092236933183/) | 2017 年独立社区个案 | 旧版结尾视频兼容性反馈，存在反例；不能作为 PM 编解码规格或普遍故障依据。 |
| [项目 GitHub](https://github.com/RepressedAlliance/AgeReVerse)、[技术来源账](../../docs/research/photon/provenance.md)、[CRmt 指南](crmt-family.md) | 当前 worktree 起点 401e9ff；本机历史 2026-09-26 探针 | 复用现有 RUO 合并、Cr6Ti 通用码字、原生解码验证思路；CRmt 缩放层不是视频帧。 |
| [Dreamcast FMV Auto-Subber](https://github.com/DerekPascarella/Dreamcast-FMV-Auto-Subber) | README 1.7（2025-05-17）；阅读作者脚本 | 保持尺寸／显示比例、字幕时序并回封装的实践。SFD 工具不能写 CRsi。 |
| [SofdecVideoTools issue 16](https://github.com/Firebow59/SofdecVideoTools/issues/16) | 用户的游戏内黑屏／挂起反馈 | 离线可播不等于目标游戏兼容；属于另一引擎、另一平台个案。 |
| [ProPainter](https://github.com/sczhou/ProPainter) | ICCV 2023 作者代码／README | 光流、传播与时序修复可供文字清除阶段评估；不是无损保证，也不承担 CRsi 编码。 |

检索包含 rUGP/CRsi/alterdec、同类游戏视频重封装及连续帧修复方向。
在本次已检索范围内未找到直接面向该 PM CRsi 演出的现成汉化写回工具。
这一结论不排除未公开、未索引或其他版本已有实现。
未上传游戏资源，未调用收费服务，未执行第三方补丁。

## 已核实的本机对象

目标 EXE SHA-256：`8e442f263feed7b79e5ccb83c3f26b12cc12e1953fb4a262b4bb74017d6e26b8`。
以下偏移均位于 `photonmelodies11.rio`，尺寸均为 1024×600。

| 字节偏移 | 帧数 | 证据与剩余边界 |
| --- | --- | --- |
| 27493704 | 1905 | ICI 明确标记 CRsi；旧独立帧包含眼球、手臂和底部英文字幕。 |
| 117665112 | 1875 | ICI 明确标记 CRsi；同类演出另一版本，差异仍待完整对照。 |
| 1715679260 | 1904 | 旧截图匹配的无底部字幕版本；本次已顺序解码全部 1904 帧。 |
| 1808635048 | 1874 | 同类无底部字幕版本，差异仍待完整对照。 |

初始 ICI 目录输出只有 5 个顶层 CRsi；不能用其数量代替全卷内嵌对象枚举。
四个候选的范围由帧表闭合计算，后两项还需补全父对象引用／语言选择证明。
旧 38 个动画中部采样及两个失败不属于完整解码证据。

## 数据与原生代码证据

- 本次支持的父头 26 字节；尺寸位于 10/12，rate 字段位于 18，帧数位于 24。
  其余未解释字段逐字保留并限制为已观察值。rate=3000；导出的 30fps 代理仍需
  结合父对象播放时钟确认，不能据此宣称音画同步通过。
- 原模式 `0x0575`、parameter=8：帧表 15 字节，结构 `B I H H H I`。
  独立帧标志位为 1，依赖帧为 0，末尾 I 为载荷长度，offset 相对载荷区起点。
- `0x0582C70` 原生帧反序列化已在离线内存中复核：codec selector 为
  `(mode >> 10) & 7`；只有 selector=1 携带额外两字节参数。
  `0x016D` 行为 13 字节 `B I H H I`。把所有行固定写成 15 字节会错位。
- PM `0x576640` 播放分派：原模式走 `0x5B8AD0`（独立）／`0x5B9450`（依赖）；
  selector=0 的独立帧走 `0x579B30`。初始化函数为 `0x403600`、`0x403A20`。
- 新探针 writer 使用 selector=0、6/6/6 色深 `0x016D`。继承 Cr6Ti 码字写入器，
  **不继承其颜色预测模型**：实际为顺序饱和的共享、蓝、红增量。
  32×16 固定随机彩色输入通过原生解码，在量化目标上 1536 个颜色字节全部一致。
  每通道最多损失 3；这只是可控编码探针，不代表生产画质获准。
- 四个完整原始记录均完成 parse→rebuild 字节完全相同验证。
  1024×600 的真实第 1140 帧重编码后，原生解码与编码器预期完全一致，
  对原 RGB 的最大通道差为 3。只替换这帧（1141 是原独立帧）后，其他帧载荷均保持原字节。
- 已把该实验 CRsi 合并进本机现有汉化 RUO 的副本：原 30 条映射与其数据区逐字不变，
  新增原对象键 `0xBC8C36D8` 后为 31 条；从新映射取出的完整 CRsi 与候选相同。
  这是离线封装证明，**尚不证明 CRsi 的游戏流式读取已经走通 RUO 重定向**。
  [可公开的探针结果](../evidence/photon/video/rebirth-probe-20261010.json) 不含游戏像素。
- 原模式输出的高字节不是统一 PNG alpha；离线代理明确按 BGRX 取 RGB，
  不把该字节当透明度。实际表面混合方式仍需父演出链路核实。
- 修改一帧后，直到下一个原独立帧之前的依赖帧必须重建，否则使用了错误预测状态。
  `rebuild()` 对遗漏的依赖帧直接报错；未修改载荷保持原字节。

## 工具及验证

[`crsi.py`](../formats/video/crsi.py) 解析／重建限定父头与混合宽度帧表。
[`crsi_literal.py`](../formats/video/crsi_literal.py) 是上述实验帧编码器。
[`native_crsi.py`](../tools/video/native_crsi.py) 用合法本地 EXE 作为独立离线 oracle；
它先锁定 EXE 哈希，只模拟解码叶函数，不启动游戏、不访问存档。

```powershell
python -m unittest rUGP.tests.formats.video.test_crsi -v
```

真实素材、完整无损离线代理、帧哈希、试验和反汇编保存在任务私有工作目录，
不提交游戏像素或 EXE。必要后续：父引用与音频闭合、原键 RUO 流式读取验证、
完整文本对照、生产画质／连续帧检查及限定实机验收。
