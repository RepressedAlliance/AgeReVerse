# 参与贡献

[返回首页](../../README.md) · [贡献者与致谢](CONTRIBUTORS.md) · [本地化制作](../../localization-make-games-speak/README.md) · [资产地图](../research/asset-map.md)

欢迎反馈问题、校对译文、补充术语、完善文档和工具，也欢迎研究其他语言的本地化。**没有必须先完成整章、提交全套测试或提供安装包的参与资格要求。** 一个可说明、可复核的小修正也可以提交。中文和英文 Issue／PR 都欢迎。

懂日语可以从 [ParaTranz 对应项目](../../localization-make-games-speak/paratranz-keep-improving-together/README.md)参与；不懂日语也欢迎反馈错字、残字、显示或安装问题，QQ群 **273626767**。

## 从哪里开始

| 内容 | 位置与方法 |
| --- | --- |
| 文本翻译／校对 | [文本流程](../../localization-make-games-speak/text-ai-translation-worth-reading/README.md)与本作译文目录，保留身份、源摘要及控制符 |
| 图片汉化 | [图片流程](../../localization-make-games-speak/images-make-it-look-native/README.md)，按实际用途分组，制作方先自检、维护者最后审核 |
| 字体／术语 | [字体](../../localization-make-games-speak/fonts-that-fit-the-game/README.md)、[现行术语](../../localization-make-games-speak/glossaries-keep-it-consistent/README.md)，按游戏与用途选择 |
| 提取、写回、运行时 | AGE2 放 [AGE2](../../AGE2/README.md)，Photon／RIO 放 [rUGP](../../rUGP/README.md) |
| 来源调查／历史资料 | [研究记录](../research/localization/README.md)，不混入现行制作清单 |
| 新语言 | [新语言指南](../../localization-make-games-speak/text-ai-translation-worth-reading/new-locale.md)，建立独立目标，不覆盖现有日文依据或中文 |

不熟悉目录可以先提 Issue，维护者协助定位和整理。尚未完成的工具或研究结论也可以发 draft PR，说明可用范围与剩余问题；不要把未验证的功能写成已经支持。

## PR 需要说明什么

说明改了什么、为什么，以及直接相关的验证结果。译文修正给出游戏、场景和理解依据；图片修正展示对应位置；工具说明触发条件和修改后的行为。没有实机结果就如实说明，由维护者判断是否需要补测。

- 文档、入口和措辞：核对内容及链接，无需各游戏全套测试或回滚演练。
- 译文、术语及同步数据：检查受影响的身份、结构、控制符与术语；改变实际显示时再查对应场景。
- 工具行为：从对应现有测试开始。只有风险、失败或依赖变化需要时，才扩大验证；不为重复实现而新增测试。
- 引擎／运行时／安装行为：按对应引擎要求做格式、平台和必要实机检查，不能用文档检查替代。

CI 的必要检查仍需通过；[检查范围](ci-checks.md)按文件类型区分。历史审核账本用于保存决策链，不是冻结所有未来译文的白名单。格式、资源绑定、冲突检测与实际适用版本等必要约束保留。

## 工具怎样进入维护范围

优先复用现有工具，小工具只解决明确需要。正式写入工具要防止错版本、错资源和覆盖输入，公开 CLI 与依赖，并验证相应输出；只读调查脚本可以先作为研究证据，不必假装是通用打包器。一次性探针和已放弃方案提炼为研究结论或必要回归，不放进日常工具目录。

## 公开内容与来源

不提交凭据、私人通信、工作站路径、完整游戏容器、官方二进制／字体或批量原始图片。结构测试使用小型合成素材；来源不可公开时保留可复核身份、摘要和提取方法。图片、字体及第三方素材说明实际来源与许可，代码 MIT 许可不能自动授权这些资源。详见[资产与发布规则](asset-and-release-policy.md)。

君望旧译及校对材料遵守已确认的公开范围，不能因整理术语或样例而夹带完整文本或能重建全文的数据。[君望入口](../../AGE2/games/kiminozo/README.md)。

## 常用检查

修改工具时安装仓库依赖，再运行相关测试；下面是各组入口，不是每个 PR 都必须逐条执行的清单。

```powershell
python -m pip install -r requirements-dev.txt
python -m unittest discover -s localization-make-games-speak/tests-catch-problems-before-players -p "test_*.py" -v
python -m unittest discover -s AGE2/tests -p "test_*.py" -v
python -m unittest discover -s rUGP/tests -p "test_*.py" -v
python -m unittest discover -s docs/research/localization/tests -p "test_*.py" -v
python .github/scripts/verify_repository.py
```

Photon 原生代码构建按 [runtime README](../../rUGP/runtime/README.md)使用对应工具链；仅改中文文案、文档或共用图片流程不要求编译无关 DLL。

<details>
<summary>English · contributing</summary>

Small, reviewable corrections are welcome. There is no prerequisite to finish a chapter, run every engine suite or provide a patch package. Explain the problem, resulting behavior and relevant verification; document real limitations. Start with affected tests and expand only for a concrete dependency or risk. Draft PRs can share incomplete research with a clear scope. Preserve stable resource identity and control codes, and do not submit proprietary dumps, private material or credentials.

</details>
