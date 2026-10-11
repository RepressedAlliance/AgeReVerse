# 中文 UI 与场景图：保留美术，重建文字关系

[技术案例](README.md) · [图片制作流程](../../../Localization-MakeGamesSpeak/Images-MakeItLookNative/README.md)

## 按本作画布与用途排版

同样叫“传输 HUD”，TDA02 的原图为 626×175，TDA01 为 818×271。直接复用文字区域会留下日文或使中文重叠、裁切。共享样式可以复用，清除区域、锚点与行宽必须从各作原图确定。

菜单保留原英文主体，将中文放回原日文副标题区域。量取不透明字芯而非整个光晕来确定字高；字芯、宽光晕和近距离辉光分别处理。常态与悬停采用相同尺寸和锚点，只改变特效，避免文字跳动。普通标题、Main Menu 和标题按钮按各自原版对齐方式处理。

地图保留原标识并额外加中文时，本项目用全角括号 `（…）` 表明补注；完全替换的按钮、名牌和 HUD 不加括号。括号的宽度应进入配方计算，不能在已导出的成品上临时补贴。地图线条、编队代码、动画和遮挡仍需按实际调用检查。

实现入口：[UI 副标题](../../tools/images/ui_zh.py)、[操作说明](../../tools/images/manual_zh.py)、[开场模板](../../tools/images/boot_notice_template.py)。实际用字见[字体与图片样式](../../../Localization-MakeGamesSpeak/Fonts-ThatFitTheGame/images.md)。

## 覆盖清单来自原版调用，不只来自旧补丁

TDA02 的大上律子登场图在日英原版都有可见图片；早期迁移仅枚举旧补丁已有文件，因此漏掉了它。旧覆盖文件缺失不能证明日文原图不存在，也不能证明最早版本一定不显示：它可能回退到原包。

新增语言资源应对照原包、脚本和当前资源选择逻辑建立清单。把原图、旧覆盖、中文候选和实际安装包的路径分别看清，再判断缺译或漏接入。

## 零字节图片也有可能是纹理索引

帝都影片序列中的部分 `.webp`／`.txb` 条目为零字节，同名 `.webp.txb.zstd` 存放实际 GPU 纹理。普通图片解码失败时，先检查配套纹理与脚本用途，不直接计为坏图、漏解或漏翻。发现字样后再按[翻译原则](../../../Localization-MakeGamesSpeak/principles.md)判断应译范围。

## English

Reuse a style, not another game's image geometry. Preserve artwork and stable hover anchors, calculate annotation width from the actual canvas, and build coverage from original script references rather than the previous patch alone. Some zero-byte image entries are placeholders paired with GPU textures; decode failure alone does not establish missing localization.
