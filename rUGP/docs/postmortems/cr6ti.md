# Cr6Ti extent correction

## Symptom

An early runtime candidate redirected one byte more than the serialized Cr6Ti
object. It displayed because the decoder obeyed the payload length and ignored
the trailing zero, but “the game tolerated it” was not an exact format proof.

## Serialized extent

The standard records in the 光子之花 image authority use:

```text
0x2C-byte header + payload_length bytes + 00 00 trailer
```

Archive-unit alignment follows the record physically, but is not part of the
record extent stored in a RIO directory or RUO redirect. For the controlled
QuickSave replacement the values were:

```text
header                 44
payload             26,821
serialized trailer       2
record extent        26,867
placement padding         1
placement span       26,868
```

The supported standard profiles include kind3/flags7, kind2/flags7 and
kind2/flags15 with a two-byte zero trailer. Two known legacy records use a
distinct 0x28-byte kind2/flags3 header with no trailer. Identify the profile
before calculating extent; the legacy shape does not make the standard
trailer optional.

## Production rule

- Compute serialized extent from the identified profile; never include generic
  archive alignment.
- Treat the two legacy records as explicit exceptions, not evidence that the
  standard trailer is optional.
- Decode official input, encode candidate, decode independently, and compare
  full RGBA plus consumed payload bytes before building a RUO.

The strict implementation and synthetic regression tests live in
[`rUGP/formats/images/`](../../formats/images/README.md). Runtime tolerance is
recorded as historical evidence, not promoted into the writer contract.
