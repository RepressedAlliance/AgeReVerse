# 切换语言后，文字为什么还停在上一种字形

[运行时](../../runtime/README.md) · [技术案例](README.md)

## 文本相同，缓存仍可能需要刷新

“山口提督”“音量”等文字在中日文中可能完全相同。原生缓存仅比较字符串，或字符串与字号时，语言改变不会使它失效，结果沿用上一语言的字形。应将有效语言纳入文字对象的刷新条件，在语言变化后重新生成，而非每帧强制重绘。

帝都的 ADV 与 GUI 缓存有不同入口。TDA 也应按自己的调用链验证，不能把另一作品的 RVA 补丁直接套过去。现行 TDA GUI 处理见 [tda_gui_locale.js](../../runtime/hooks/tda_gui_locale.js)；各层语言编号见[运行时说明](../../runtime/README.md)。

## 原生持有的内存，要有匹配的生命周期

脚本为原生代码分配语言映射表后，如果只在局部作用域保存对象，垃圾回收可能释放原生仍在使用的地址。应保留对应分配对象的引用，直到原生不再使用；不能只保留一个裸指针值。

## 文件选择与长度必须属于同一份资源

重定向读入了新 EGPACK，而目录枚举仍返回旧文件长度，会出现 `Text ID Not Found` 或不完整读取。资源路径、枚举长度与实际字节必须同步。完整路径过长时，加载失败也可能静默回退原包；应检查引擎实际使用的完整路径，而不只检查相对文件名。

## 实机复查的重点

同一句切换语言、相同文字切换字体、图片后缀恢复、字幕清除和旧存档摘要分别检查。原版 Log 会按框宽重新折行，读档或切换语言也可能改变历史记录；本地化应先对照原作行为，再决定是否修复，不能把差异一律归因于漏句。

## English

Include the effective locale in text-cache invalidation even when the string is unchanged. Keep script-owned allocations alive while native code holds their addresses. Resource redirection must also provide matching enumeration lengths and valid complete paths. Test each game's actual call sites and compare backlog behavior with the original.
