# CRsa 文本提取：找得到字符串，还要认得它的用途

[文本工具](../../tools/text/README.md) · [CRsa 格式](crsa-text.md)

## 从对象和命令读取字段

CRsa 不只有正文字符串池。`CVmMsg3` 的每种语言都包含正文、批注和指令三个字段，调用参数、变量绑定和计数字符串也可能带文字。按可读字符扫描会同时漏掉控制源槽下的显示文本，并把旧池残留或程序标识符当成漏译。

原生解析器 [crsa_vm_stream.py](../../formats/rio/crsa_vm_stream.py) 从 24 字节头部顺序读取，共享类／对象缓存，并按 [类型 schema](../../formats/rio/crsa_vm_schema.json) 解释消息、调用、跳转、音声和绘图命令。未知类型、版本、越界字段或非零未解析尾部应停止解析，不能跳到下一个看起来像文字的位置继续。

## 正文、批注与未引用池单元分开

正文没有可见日文，不表示显示槽也为空。光子之花训练场开场和光子旋律打西瓜提示就使用控制源槽与可见显示槽。应按真实 `CVmMsg3` 引用提取，保留源槽的空白／控制身份。

批注位于 `CVmMsg3.first_records[language][1]`。相邻池单元只能提示调查方向，不能证明引用关系。遇到失效或冲突索引时，记录未绑定状态，再结合原生字段和场景重绑定；未引用的旧尾部不能自动加入对白。

源槽在自己的原生索引处结束。不要跨 NUL 借用下一句，也不要让索引 0 冒充第一条有字的台词。字段摘要按对应存储约定计算：池槽的终止 NUL 与计数字符串内部的码元不同；比较时明确原编码字节与历史 UTF-8 摘要的区别。

## 有文字的参数，也可能不能翻译

`OM_AccessWrite`／`OM_AccessGetValue` 的键值需要沿被调用脚本确认。动作名称可能直接进入引擎注册表，见[“返回游戏”按钮失效](backlog-return-action-20260910.md)。不能仅按大小写或含日文决定处理。

本项目另明确保留经 `OM_TWF_SetArm.兵装名` 传入 `CTWFRemainderBox` 的 260 处兵装名参数。这是已区分用途的范围选择，不是 260 句漏译；它们不进入显示正文写回。字段定位实现见 [crsa_vm_fields.py](../../formats/rio/crsa_vm_fields.py)。

## 维护稳定身份

同一原文可能出现多次，应核对各次原生引用。旧审校 ID 的坐标与新解析字段相撞，也不代表内容相同；来源摘要不同则建立新身份，保留原记录。控制符、换行、说话人包装和正文措辞分别比较，不能把“源摘要匹配”解释为“现行译文逐字一致”。

原生字段解析只说明固定版本中静态存储的字段范围，动态生成文字、其他脚本格式和实际可达路径仍需另查。写回见[原生文本与存储路线](crsa-writeback.md)，现行文本从[章节表](../chapter-texts.md)进入。

## English

Parse native objects and references, not readable byte runs. Message body, annotation, instruction, call parameters and unreferenced pool residue have different roles. Preserve empty/control source identities and stable review IDs; never infer an annotation reference from adjacency or translate an engine action identifier as display text.
