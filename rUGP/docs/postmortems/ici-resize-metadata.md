# ICI growth: duplicate sizes and preserved wrapper metadata

An enlarged Photon RIO can change the ICI allocation-bitmap length. Regenerating its encrypted wrapper as a generic length header produced a candidate that decoded locally but could lead to a white screen. The clean files carried `3` in the second header word's low three bits; the faulty helper substituted `7`.

`CInstallSource` also stores the final RIO size twice. Updating only one field leaves the object inconsistent.

## Rebuild the derived metadata

1. Decode the exact clean encrypted wrapper and payload.
2. Update both serialized RIO-size values.
3. Extend the allocation bitmap only with zero bits implied by the new block count.
4. Rebuild the redundant encrypted size header for the new plaintext extent.
5. Inherit the clean second word's low three metadata bits exactly.
6. Independently decode both sizes, the bitmap and all unrelated archive references.

An unchanged input should produce byte-identical output. Treat bitmap growth boundaries and unknown wrapper bits explicitly; do not repair a generated candidate by guessing convenient defaults.

## Supported boundary

This is a static repair method, not a general production ICI writer with confirmed runtime acceptance. A future writer needs duplicate-size, bitmap, low-bit inheritance, no-op and independent-decoder tests, followed by actual game checks for the targeted version. See [image transport](image-transport-runtime.md) for alternative routes.
