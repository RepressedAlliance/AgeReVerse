# 多语言源槽关联：先确定同一句，再判断译文

[本地化资料](README.md) · [来源规则](../../../Localization-MakeGamesSpeak/Text-AITranslationWorthReading/02-source-data.md)

日文、英文和中文在同一容器中，不代表可以仅按显示顺序配对。提取与写回要保留记录身份、语言索引、脚本引用和日文源摘要；不同版本的索引必须先对齐，再比较译文。

## PM 的一项历史关联疑点

2026-09-08 的记录指出，`pm:vm:photonmelodies11.rio.004:655753292:00031180:00157` 的日文是武谈论天气，英文却是霞谈论不妙的情况，中文对应英文内容。该记录没有给出槽位修复结果或适用的玩家补丁版本，应继续作为待核关联问题。

不能只把说话人“霞”改成“武”：先核对原始语言索引、脚本调用和场景语音，再判断究竟是提取配对、源槽本身还是译文错配。此条疑点也不能推广为其他正常姓名映射有误。

## English

Align stable record identity, language indices, script references and Japanese source hashes before comparing multilingual text. The dated PM example above remains an unresolved source-association question with no confirmed affected player release; changing only the speaker name would not resolve the underlying mismatch.
