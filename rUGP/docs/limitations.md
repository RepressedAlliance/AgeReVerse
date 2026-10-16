# Photon 组件适用范围与未解决事项

[rUGP](../README.md) · [玩家版本](../../docs/player/README.md) · [技术案例](postmortems/README.md)

## 选择版本时看什么

光子之花／光子旋律工具和运行时按固定 Steam EXE、归档和字体身份工作，不支持任意 rUGP 版本。源码的默认构建、显式候选选项与玩家发布包不是同一份配置，具体对应见[运行时](../runtime/README.md)与相应 Release。

路线目录中的 1,490 项是基线图片的逻辑来源分类，另有西瓜教程复合帧增补。逻辑路线已知不等于全部最终图片、字体及私有构建输入都已公开，也不等于所有场景都完成了实际显示检查。当前公开包构建范围见[打包说明](../packaging/README.md)。

## 保留的问题与覆盖缺口

| 范围 | 已知情况与下一步 |
| --- | --- |
| PF 部分页面偶发英文 | BETA 0.1.2 的已知问题，尚未彻底解决；反馈时附场景、存档及语言设置 |
| PM／PF 剧情视频 | BETA 0.1.2 尚未包含再诞双段字幕、回顾标题及倒计时的[当前制作成果](photon-video-scope.md)。再诞原作英文技术图形保留，新增旁白字幕另行汉化；下一版只完成[接入规划](../packaging/video-integration-plan.md)，未制作最终玩家包 |
| CRip008 的 40 个未观察调用 | 精确长度回放通过，实际补齐参数仍未观察到；不是 40 个已确认故障。入口和资源身份见[定位说明](postmortems/pending-hook-entry-points-20260909.md) |
| PM 四项只见加载的提示 | 三项手柄 UI 与一项壁纸解锁提示，需确认实际绘制条件 |
| HUD 英文画面 | 日文图片模式也含英文；具体素材对应关系待核验，不能只按语言判定 hook 错误 |
| PF 保守行宽预算 | 块 `488631608` 的命令顺序 3、6、39 曾超出离线预算；样本反馈良好，不能直接认定溢出，仍需覆盖实际上下文 |
| PM 日英槽差异 | `.004:655753292`、命令偏移 `31180`／顺序 157 的日文说话人为武，现行中文跟随英文槽的霞；源／场景关系未解决，见[源文对齐](../../docs/research/localization/source-alignment.md) |
| 历史术语差异 | 部分角色音译、军衔和 HIVE 分类需结合现行表确认，见[术语选择](postmortems/terminology-20260908.md) |
| ICI 增长 | 重复长度和包装头修正有静态方法；尚不是已获实机确认的通用生产写入器 |
| 全路线与组合显示 | 已修复案例的样本通过，不替代每个资源、旧存档、语言切换、批注及演出时机的完整覆盖 |

## 已处理案例与影响范围

“返回游戏”动作参数误翻译、PM 相册 selector 失效、PF 祭典补齐／局部矩形、玩家包索引排序、PM 特殊字体指令和 PF 正文／批注缺字分别有[独立案例](postmortems/README.md)。查问题时匹配受影响版本与资源；旧候选问题不能自动套到后续已修正的玩家包。

## English

Support is tied to exact builds and resource identities. BETA 0.1.2 still has intermittent English pages in PF and does not include the current story-video localization candidates. The candidates retain original English technical artwork and localize added narration captions, recap titles and countdown labels; final package integration is planned separately. Unobserved calls and conservative layout warnings are not confirmed defects. Preserve unresolved source alignment and runtime-entry questions, while checking each incident's affected version before treating it as a current release bug. The public components do not provide every private input or exhaustive in-game coverage.
