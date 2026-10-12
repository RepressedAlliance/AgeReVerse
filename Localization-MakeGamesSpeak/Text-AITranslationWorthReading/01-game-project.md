# 01 · 单个游戏项目清单

[规则顺序](README.md) · 下一步：[02 源数据](02-source-data.md)

每个受支持游戏在 `AGE2/games/<game>/` 或 `rUGP/games/<game>/` 下保存一个
`project.toml`。它是面向人和自动检查的入口，不替代翻译表、图片清单、构建脚本或
Release manifest。

清单统一回答：

- 这是什么游戏、使用哪套引擎、对应哪个 Steam App ID；
- 当前维护哪些目标语言；
- 玩家包是历史测试版、开发中还是可推荐版本；
- 当前 `player_release_tag` 与玩家版本索引对应；历史图片清单用 `image_authority_scope` 标明，不冒充该发布版逐图清单；
- 正文、术语、图片和字体的权威文件在哪里；
- 图片是否需要按光子之花／光子旋律等过滤条件读取共用清单。

接手项目时，还要从本作 README、资源清单或现有备注确认[内容与功能、原意依据、呈现方案、制作底稿和交付目标](../principles.md#中文版的定位与制作范围)。先关联同一场景的文字、语音、图片及各版差异，再确定中文制作范围；某版缺少同形式资源不等于缺少原作内容。这里复用现有记录，不要求给 `project.toml` 增加一套必填字段。多个交付对象仍分别保留实际身份和调用。

所有相对路径都以该 `project.toml` 所在目录为基准。目录不存在时不要创建空壳；把
未完成状态写进清单和游戏 README。路径指向的文件必须进入 Git，并由测试在 Windows
和 Linux 上检查大小写。

`engine` 是展示与边界名称，只允许 `AGE2` 或 `rUGP`。具体序列化协议、命令行选项或
历史 schema 内已有的 `age2`／`rugp` 小写标识属于兼容接口，不应为了展示统一而改写。

## English summary

Use each game's existing manifest and README as the entry point. Establish the
content/function scope, meaning evidence, presentation, authoring base and
delivery targets through existing resource lists or notes; no new mandatory
TOML fields are required. Link the same scene across text, audio, imagery and
official editions before selecting production tasks. Missing same-form assets
do not establish missing original content. Preserve every actual target's
identity and calls, as well as the existing manifest and schema contracts.
