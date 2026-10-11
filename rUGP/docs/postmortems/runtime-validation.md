# 图片运行时检查：验证写入行为，而不只验证图片能打开

[图片工具](../../tools/images/README.md) · [格式与传输](image-transport-runtime.md)

## 让测试经过实际生产入口

PNG 正确、摘要匹配，不表示游戏最终会显示它。回归应调用生产 `prepare/commit` 与实际查找表，而不是另写一段等价的复制代码。准备阶段不改目标；模拟原解码器写入后再提交，检查使用的背景来自准备时刻，并验证 RGBA 到引擎透明度域的转换。

按绑定分别覆盖直接／索引入口、正／负 stride、紧密／带行尾 padding、直接复制／透明度合成，以及有效和无效矩形。检查行尾与缓冲区外保护字节，部分图只能写入获准矩形。

准备到提交之间改变源载荷、身份、对象或语言状态时，旧事务必须失效。命中数量不能代替每个绑定的结果，空结果也不能因 `all([])` 而判为成功。

## 补齐长度需要真实调用依据

归档 payload 长度、序列化记录长度和解码调用方长度不是同一值。光子之花祭典实际携带三字节尾部补齐，详见[全图与局部图案例](pf-festival-presentation-20260909.md)。只接受已观察到的长度及完整身份，不能为测试全部变绿而扫描任意前缀或放宽补齐。

历史回放中仍有 40 个绑定未观察到实际补齐参数；构造的额外长度失败不是 40 个已确认坏图。后续按[资源入口](pending-hook-entry-points-20260909.md)找到实际场景，再决定是否需要修改。

## 原生调用与合成内存分开检查

安装前确认精确 EXE、调用点指令、目标和 selector 条件；单字节破坏应被拒绝。汇编包装还需检查参数、返回值、栈平衡、非易失寄存器和在途计数。关闭写入门的转发测试不证明开启门之后的完整生命周期。

合成 owner、背景和解码写入可以隔离事务错误，但没有执行私有解码器，也没有经历真实初始化、对象图和剧情分支。日志按精确资源身份区分“加载”“绘制”“提交并回读”“拒绝”和“未触发”，不把其他图片命中或外观相近的相册图当成目标已通过。

## 包装完成后重新检查交付表

打包可能生成不同于仓库基线的新表。使用最终交付 include root 执行查找及图片装载，覆盖全部数值键、顺序与重复项。实际回归见[图片索引排序](player-image-index-20260910.md)。

可复用入口见 [replay_cr6ti_routes.py](../../tools/images/replay_cr6ti_routes.py)、[replay_crip008_routes.py](../../tools/images/replay_crip008_routes.py)、[verify_native_sites.py](../../tools/images/verify_native_sites.py) 和 [verify_pm_production.py](../../tools/images/verify_pm_production.py)。数据目录保存相关输入描述与回归样本，不替代对应版本的实际游戏观察。

## English

Exercise production lookup and prepare/commit, including stale transactions, signed strides, partial rectangles and unchanged guard bytes. Authenticate the complete caller buffer; padded lengths need observed identities. Synthetic execution, native ABI checks and actual scene observations cover different behavior. Recheck the generated delivery tables after packaging.
