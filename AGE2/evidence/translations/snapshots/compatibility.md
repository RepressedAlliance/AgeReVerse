# Translation snapshots and release compatibility

[AGE2](../../../README.md) · [Review data](../review-ledger/README.md) · [Current scope](../../../docs/limitations.md)

The public CSV tables are maintained translation sources bound to exact Japanese source identities. A runtime contract describes how those records are loaded; a Release payload is the particular package shipped to players. These roles should not be treated as interchangeable.

## What can be rebuilt

TDA00–03 provide a strict source-hash join from public dialogue tables to locally extracted EGPACK data. Imperial also provides a non-dialogue builder. These components alone do not reconstruct every speaker, choice, image, font, UI resource or byte of a historical ZIP.

Current tables and historical packages contain different revisions. Later commit dates alone do not decide which wording is correct, and replacing a whole table with an old branch can restore old mistakes or lose later corrections.

## Comparing a specific release

1. Identify the exact Release tag and package, then extract its localized fields.
2. Join by stable resource path, record ID and language slot; handle dialogue, speaker, choice and ruby records separately.
3. Resolve differences using Japanese source and scene context, the reviewed decision and the shipped value.
4. Bind the resulting table to that package version and verify the rebuilt resources and affected scenes.

A released Chinese field is a comparison input, not the original Japanese source. Keep unresolved differences explicit; do not fill them from an unrelated staging tree.

## 中文

现行译文表、运行时读取约定和历史发布载荷各有不同用途。当前公开链路可复用部分组件，尚不能逐字节重建所有旧包。比较版本时按稳定记录身份逐项解决差异，不因文件较新或较旧就整表覆盖。
