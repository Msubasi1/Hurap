# HuRAP — Cryptographic Mission

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modular Python program that performs a three-stage cryptographic mission on the encoded "HuRAP" message: decrypt it, infect it with a virus, then re-encrypt the result. Built as a programming assignment using only the Python standard library.

## Story / Overview

The narrative framing of the assignment: an encrypted message ("HuRAP") arrives in binary, and a sequence of operations must be applied to recover and transform it. The program is split into three missions executed end-to-end:

- **Mission 00 — Decrypt the HuRAP**
  Read the raw binary message, group bits into bytes, convert to hexadecimal, look up each hex pair in a custom character table (`schuckscii.txt`), and finally apply a Caesar-style shift cipher to recover the plaintext. The shift amount itself is encoded as a two's-complement integer in the first non-binary line of `hurap.txt`.

- **Mission 01 — Inject the virus**
  Apply a set of find-and-replace rules from `virus_codes.txt` to the decrypted text. Example rules:
  `kill → self-destruct`, `for → while`, `Hacettepe sucks → Hacettepe is the best`.

- **Mission 10 — Re-encrypt the virus-infected message**
  Apply the inverse Caesar shift, look up characters in the custom table to produce encrypted glyphs, then convert back to hexadecimal and finally to binary — closing the loop.

## Features

- **Pure Python 3** — uses only `sys` from the standard library
- **Modular design** — each mission is a separate file
- **Two's-complement key parsing** — decodes signed shift amount from binary
- **Custom character table** (`schuckscii.txt`) — bijective hex ↔ printable-char map
- **Deterministic verification** — bundled `expected_output.txt` for diff testing

## Tech Stack

- **Language**: Python 3.6+
- **Modules used**: `sys` (stdlib only)

## Project Structure

```
.
├── src/
│   ├── hurap.py            # Entry point — orchestrates the three missions
│   ├── FileReading.py      # Binary read + hex conversion (Mission 00 prep)
│   ├── Mission00.py        # Encrypt / decrypt / two's-complement key recovery
│   ├── Mission01.py        # Virus injection (pattern-based find/replace)
│   └── Mission10.py        # Inverse encrypt + hex + binary serialization
├── hurap.txt               # Input: binary HuRAP + key line
├── schuckscii.txt          # Custom char ↔ hex table
├── virus_codes.txt         # Find/replace rules for Mission 01
├── expected_output.txt     # Reference output for verification
├── Hurap.pdf               # Original assignment specification
├── requirements.txt
├── LICENSE
└── README.md
```

## Installation

```bash
git clone https://github.com/Msubasi1/Hurap.git
cd Hurap
```

No external dependencies are required. A Python 3.6+ interpreter is sufficient.

## Usage

The entry script imports its helpers from the `src` package, so run it as a module from the project root:

```bash
python -m src.hurap hurap.txt schuckscii.txt virus_codes.txt
```

Compare against the bundled reference output:

```bash
python -m src.hurap hurap.txt schuckscii.txt virus_codes.txt > my_output.txt
diff expected_output.txt my_output.txt
```

### Expected output (excerpt)

```
*********************
     Mission 00
*********************

--- hex of encrypted code ---
...

--- encrypted code ----
...

--- decrypted code ---
...

*********************
     Mission 01
*********************
...
```

See `expected_output.txt` for the full reference.

## How It Works

| Mission | Input | Operation | Output |
|---------|-------|-----------|--------|
| 00 (a) | `hurap.txt` binary lines | Group into bytes → hex | Hex representation |
| 00 (b) | Hex pairs | Lookup in `schuckscii.txt` (col 2 → col 1) | Encrypted glyph string |
| 00 (c) | Key line of `hurap.txt` | Strip non-binary chars → two's complement | Signed shift amount |
| 00 (d) | Encrypted glyphs + shift | Caesar shift over 94-char table | Decrypted plaintext |
| 01 | Decrypted plaintext + `virus_codes.txt` | `str.replace` per `key:value` line | Infected plaintext |
| 10 (a) | Infected plaintext + inverse shift | Reverse Caesar shift | Re-encrypted glyphs |
| 10 (b) | Glyphs | Lookup in `schuckscii.txt` (col 1 → col 2) | Hex |
| 10 (c) | Hex | Binary representation | Final binary string |

## Author

**Muhammet Subaşı** ([@Msubasi1](https://github.com/Msubasi1))

## License

Released under the [MIT License](LICENSE).
