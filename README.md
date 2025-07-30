# hex_crc16_calculator

[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

Python tool for calculating **custom CRC16 checksums** from space-delimited hexadecimal text files. Processes nibble-based lookups with byte-swap output.

## Features
- 🚀 Parses space-delimited hex values (e.g., `01 A2 FF 0C` or `1 A2 FF C`)
- ⚡ Implements **4-bit lookup table algorithm** (non-standard variant)
- 📊 Real-time intermediate CRC display per byte
- 🔄 Automatic byte-swap final output

## CRC16 Specification
| Property        | Value               |
|-----------------|---------------------|
| **Type**        | Custom algorithm    |
| **Initial Value**| `0xFFFF`            |
| **Lookup Table**| 16-element table    |
| **Processing Unit**| 4-bit nibbles       |
| **Final Transform**| Byte-swap          |

## Supported File Format
`.txt` files containing:
- Space-separated hexadecimal bytes
- Single or double-character values (e.g., `F` or `0F`)
- Valid examples:  
  `01 A2 FF 0C`  
  `4B 7F C2 8D 00 E5`

## Usage
1. **Prepare Input File**  
   Create a text file (e.g., `input.txt`) with space-delimited hex bytes.  
   Example content: `01 A2 FF 0C`  
2. **Run Command**  
   ```bash
   python crc16_calculator.py input.txt

3. **​​Output Example**
   ```bash
    File: input.txt
    Size: 4 bytes
    
    Index  Byte(Hex)  Intermediate CRC(Hex)
    ----------------------------------------
    0      01         56C1
    1      A2         D8C1
    2      FF         6B41
    3      0C         89D1
    
    ========================================
    Final CRC16: 0xD189
    ========================================

## Algorithm Workflow
   - Initialize CRC = 0xFFFF
   - For each byte:
     - Process ​​low 4 bits​​ (nibble)
     - Process ​​high 4 bits​​ (nibble)
     - Update CRC via 4-bit table lookup
   - After all bytes: Apply byte-swap to final CRC

## License
Distributed under the MIT License. See LICENSE for details.

## Installation
```bash
git clone https://github.com/your-username/hex-crc16-calculator.git
cd hex-crc16-calculator
