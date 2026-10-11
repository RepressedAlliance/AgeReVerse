# Structural empty EGPACK records

[Translation snapshots](../../evidence/translations/snapshots/README.md) · [EGPACK tools](../../tools/egpack/README.md)

An empty target is not always a missing translation. Some engine records have
no source or target text; filling or deleting them would change the resource
sequence. Control-only records that clear the current display are a separate
case and must retain their engine behavior.

## Classify before writing

Match the stable resource identity to a lawful local source export. Check the
slot's exact value and hash, rather than deciding from the displayed text or
the total number of blank rows.

The portable schema has an explicit `record_kind`:

- `text` binds non-empty source and localized text;
- `structural_empty` requires SHA-256 of the empty source, an empty local
  source slot and an empty target, then becomes a verified no-op rather than
  a text write.

A native `\f` command is not an empty string. If a local export still contains
that command, the strict empty-slot join must reject it; do not erase the
command or change its hash to bypass the check. Clear-command adaptations need
their own validated resource binding and must preserve the game's clearing
behavior.

The exporter, local-source join and regression tests enforce these contracts.
`--allow-empty` does not bypass malformed-record checks. For native clear
records and synchronization, use the [retained repair data](../../../docs/research/localization/reviews/README.md).

## Reusable rule

Preserve and classify every stable resource identity. Empty, absent,
control-only and intentionally cleared values represent different states;
one CSV blank-value convention cannot safely replace them all.
