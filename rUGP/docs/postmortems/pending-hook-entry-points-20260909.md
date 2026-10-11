# 图片调用定位：从资源身份找到真实显示场景

[图片运行时](runtime-validation.md) · [图片数据](../../evidence/photon/images/README.md)

## 仍未观察到的范围

历史调用采集中，40 条 CRip008 绑定尚未观察到实际长度／补齐参数；精确长度离线回放通过，不表示存在 40 个已知故障。光子旋律另有四项只见加载，尚不能认定已经绘制。

| 资源 | 原生引用范围 | 定位方式与限制 |
| --- | --- | --- |
| PF 18 项军事 HUD／兵装标识 | 《继承》《告白》及兵装辅助脚本；《雨舞者》《小鸡潜降兵》有部分调用 | 在驾驶舱／战斗演出按身份记录；状态和兵装选择决定实际成员 |
| PM 18 项军事 HUD／兵装标识 | 《憧憬》及两组兵装辅助脚本 | 使用对应剧情，不以相册装备说明图代替 |
| PF G2787／G2803 | 《樱花盛开之前》脚本命令 274／1948 调用背景辅助脚本 | 毕业礼堂与校门；尺寸分别为 900×700、933×718 |
| PF G1668／PM G3003 篇章 Logo | 官方映射表存在资源关系，已解析 CRsa 中无直接引用 | 显示入口仍未证明，不据此判为废弃资源 |

G1661／G1662 是静态装备说明图，G1972 是 1280×996 的相册礼堂图。它们与 HUD 或 G2787 外观相近，也不能互相代替。静态引用证明脚本包含关系，不保证播放一个片段就绘制其全部成员。

## HUD 含英文，不足以判定中文替换故障

《小鸡潜降兵》开场能到达驾驶舱，脚本关联 G2278／G2280／G2288 等候选，但观察到的 HUD 英文尚未绑定到这些具体像素来源。日文图片模式也显示 `36mm chain gun`、`120mm cannon` 和 `Armed Selection`；对白中文与图片语言设置是两回事。

因此保留“实际素材对应关系待核验”，撤回仅凭英文就认定 hook 失败的判断。未命中目标身份的解码事件或拒绝日志，不能自动解释这个画面；也不能据此改兵装参数或放宽图片匹配。

## 预加载与解锁提示

| PM 资源 | 已知入口 | 尚缺的确认 |
| --- | --- | --- |
| G2946／G2961 存取档手柄提示 | `OM_SpecifyPrefetchCommand` 的预加载 | 原生控件的绘制与输入模式入口 |
| G2971 语音回放手柄提示 | 同类预加载 | 不能通过普通相册浏览证明显示 |
| G492 壁纸解锁提示 | `PM_WPOPEN_` 状态判断后调用辅助脚本并更新状态 | 需要实际未解锁事件；反复浏览已解锁壁纸不构成显示确认 |

## 复用定位工具

```powershell
python -m rUGP.tools.images.trace_pending_script_references --census-root "<private-census-directory>" --output "<report.json>"
```

工具按已登记的 40＋4 项读取资源参数与原生命令，不是任意脚本格式的全游戏可达性分析器。字段、脚本身份和调用关系见 [pending-script-routes.json](../../evidence/photon/images/static-review-20260909/pending-script-routes.json)。定位已有存档时，使用场景和精确身份；不修改解锁状态，不为未知入口安排盲目重播。

## English

Static script references are navigation aids, not proof of a draw. Distinguish military HUDs from similar album art, prefetch from rendering, and locked-event prompts from ordinary gallery visits. The English HUD observation remains unbound to an exact source; it is not an established replacement failure.
