# 仓库结构与边界

[返回研究入口](README.md) · [资产地图](asset-map.md) ·
[贡献规范](../project/CONTRIBUTING.md)

公开仓库是一棵可维护、可复核的源码树，不是开发工作站的镜像。

君望 Steam 本篇及附加篇的项目位置为 [`AGE2/games/kiminozo/`](../../AGE2/games/kiminozo/README.md)，分别组织文本、术语与基线、UI 图片和字体。当前为制作中项目，尚无公开正文表或安装包。

## 五层结构

```text
README.md                 中文玩家首页，研究者内容在独立部分
docs/                     玩家、研究、项目维护、法律与英文入口
Localization-Make-Games-Speak/  跨引擎的本地化方法、工具和测试
AGE2/                     TDA / 帝都技术与游戏资产；君望在制项目
rUGP/                     Photon 的完整独立技术与游戏资产树
```

## 本地化制作目录

```text
Localization-Make-Games-Speak/
  Text-AI-Translation-Worth-Reading/    让 AI 翻译值得读下去；文本工作流与 01—07 规范
  Images-Make-It-Look-Native/           让中文长在原画里；五阶段制作与审核
  Fonts-That-Fit-The-Game/              别让字体出卖补丁；字体、来源和实际用途
  Glossaries-Keep-It-Consistent/        十万字也不乱套；基线、术语与全文一致性
  ParaTranz-Keep-Improving-Together/    一起磨好译文；发布后多人校对与同步
  Tools-Let-Tools-Handle-Repetition/    把时间留给翻译；按任务使用的共用工具
  Tests-Catch-Problems-Before-Players/  先替玩家发现问题；工具的对应回归检查
docs/research/localization/
                          保留的旧词库、审核记录与研究工具
```

目录名同时标明主题与读者能解决的问题。字体直接集中于 `Fonts-That-Fit-The-Game/`；各作源表与资源绑定仍留在对应引擎的游戏目录。术语入口讲解基线到全文一致性的方法，具体语境基线留在各作品的 `terminology/` 中。图片步骤不重复实现引擎提取器；工具按实际使用需求复用。

从仓库根目录运行工具时使用文档中的 `python -m` 命令。含连字符的目录由 Python 的 `importlib.import_module` 加载，包内使用相对导入；公开命令的 `--help` 与对应测试持续检查这些入口。历史研究目录 `docs/research/localization/` 保留原位置。

结构参考了 [Tsukihime Translation](https://github.com/Tsukihimates/Tsukihime-Translation) 对脚本、图片及工具的区分、[VNTranslationTools](https://github.com/arcusmaximus/VNTranslationTools) 的提取／插入接口，以及 [07th-Mod](https://wiki.07th-mod.com/developer/overview/patch-folder-structure/) 对补丁目录和部署资源的组织。这里借鉴的是职责分开维护；具体阶段、样式和人工审核要求以本项目实际制作过程为依据。

`AGE2/` 与 `rUGP/` 分别拥有自己的 `games/`、工具、测试、证据和事故记录，互不 import。
只有术语、翻译/审核方法、语言命名、图片制作与字体覆盖等真正不依赖引擎的内容进入
`Localization-Make-Games-Speak/`。

## 游戏专属内容为什么跟随引擎

一行译文或一张图片一旦带有以下任意信息，就不再是纯粹的通用本地化资料：

- EGPACK、RIO 卷、对象 offset/extent 或父引用；
- 日文／英文／translation 槽；
- `root/assets/...` 松散路径；
- Cr6Ti、CRip007、CRip008 或其他编码模板；
- 某个 App ID、EXE/DLL 哈希或游戏版本门。

这些内容必须放进对应游戏目录。`Localization-Make-Games-Speak/` 可以定义表结构、两轮审核和图片 QA，
但不能成为混杂各部游戏原始资源和 writer 输入的总仓库。逐项位置见[资产地图](asset-map.md)。

## Git、Release 与本地工作区

| 层 | 应保存什么 | 不应保存什么 |
| --- | --- | --- |
| Git | 可维护译文与术语、图片文案/身份/哈希、源码、合成测试、来源说明、长期有效的复盘 | 游戏容器、完整官方源、编译产物、缓存、一次性探针、失败批次 |
| GitHub Releases | 玩家 ZIP/安装器、对应源码可构建的 DLL、大型且通过权利审核的本地化图片包、校验文件 | 无来源字体、游戏原始包、未审查候选或把研究资产冒充玩家包 |
| 本地忽略目录 | 合法游戏安装、提取的官方源、API 凭据、原始模型响应、候选图、联系表、临时打包根 | 任何只有一台机器能解释却被当成项目权威的目录快照 |

大型本地化二进制放在同一仓库的 Releases，不会分散项目 star、Issue 或版本历史；Git 中
保留 manifest、哈希、制作规则和代码，确保下载资产仍能定位到提交和审核状态。

## 引擎边界

```text
AGE2
  pack.bin / FPD
      -> EGPACK、WebP、UI、字体
      -> 对应游戏的 LocalAppData 松散覆盖

rUGP
  ICI 目录与 RIO 卷
      -> CRsa、Cr6Ti、CRip 等完整对象记录
      -> RUO 或严格版本绑定的运行时
      -> 密封输入根与确定性打包
```

AGE2 当前不需要运行时 Hook；rUGP 也不能继承 AGE2 的松散覆盖假设。共享一个仓库不代表
共享容器、编码器、安装目录或成功证据。

## 一个本地产物何时可以进入公开仓库

至少满足：

1. 其他贡献者能说清它解决什么问题；
2. 不依赖原作者的绝对路径和临时环境；
3. 输入、输出、版本和哈希可说明；
4. 权利和许可证状态明确；
5. 它成为可运行工具、合成回归、可维护表、紧凑 manifest、确定性配方或长期复盘中的
   一种，而不是整个中间目录原样搬运。

“编译可重复”不等于“生成其配置的研究过程可重复”；“能解码”不等于“能安全写回”；
“一台机器实机成功”也不等于“已有玩家可发布包”。文档必须保留这些边界。

## English summary

The root README puts Chinese player downloads first and exposes the reusable localization guide separately. `Localization-Make-Games-Speak/` owns
engine-neutral human workflow and QA; `AGE2/` and `rUGP/` independently own
their game-bound text, image identities, formats, tools, tests, and incident
records. Git stores maintainable source and evidence, this repository's Releases
store reviewed large binaries and player packages, and lawful proprietary input
plus transient production output remains local.
