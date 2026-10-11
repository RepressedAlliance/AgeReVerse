# Sealed generated runtime configuration

## Configuration scope

The ordinary tables now contain 1,197 光子之花 routes and 1,598 光子旋律 routes in the 光子旋律
build; the 光子之花 build retains its installed companion 光子旋律 table of 1,594 entries.
Both binaries contain cross-game identities, even when a game does not use
those routes, so the 光子旋律 table uses explicit `PHOTON_BUILD_PM` conditionals to
preserve each installed binary's inputs. The special table contains 68 entries
(17 光子之花 / 51 光子旋律, including tutorial entries exclusive to 光子旋律).

Per-game source identities are recorded in `provenance.json`; headers use LF.
The PF and PM views are distinct build inputs. Do not combine files by
modification time or infer a player package's configuration from a historical
local installation. Four reserved PM identities have no image-readback claim.
See the [configuration snapshots](../../evidence/photon/images/static-review-20260909/README.md)
for the associated datasets and build manifests.

## Regeneration boundary

These six headers are reviewed, hash-locked runtime configuration inputs. They
contain identities, sizes, geometry and routing metadata, but no game image
payloads. [`provenance.json`](provenance.json) records each file's exact bytes,
SHA-256, role and any sealed source-manifest identity embedded in the header.

The important limitation is explicit: the public repository currently has no
maintained deterministic generator plus complete publishable input set for
these headers. A clean clone can verify their hashes, stage the authorization
bit in a temporary directory, compile them, and reproduce the normalized DLL;
it cannot regenerate the tables independently. They are therefore classified
as **sealed reviewed configuration**, not as publicly reproducible generated
source.

Changing a header requires more than editing its checksum. A future update
must either publish a deterministic generator and redacted/hash-bound inputs,
or repeat the private authority audit and replace this provenance manifest in
the same reviewed change. Until then, docs and build manifests must preserve
the distinction between “reproducible compile from checked-in configuration”
and “reproducible generation of that configuration.”
