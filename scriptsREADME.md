# Packing List Generator

A smart Python script to generate optimized packing lists for digital nomads.

## Installation

No external dependencies required! Uses Python 3.6+


bash

Make the script executable (Unix/Mac)
chmod +x packing-list-generator.py


## Usage

### Basic Examples

**Daily Commute:**

bash python packing-list-generator.py --type commute --duration 1


**Weekend Workshop:**

bash python packing-list-generator.py --type weekend --duration 3 --work-intensity heavy


**Long-term Digital Nomad:**

bash python packing-list-generator.py --type nomad --duration 14 --extras


### Export as Markdown Checklist


bash python packing-list-generator.py --type nomad --duration 7 --export my-packing-list.md


### JSON Output


bash python packing-list-generator.py --type weekend --duration 3 --format json


## Parameters

- `--type`: Trip type (`commute`, `weekend`, `nomad`) - **Required**
- `--duration`: Number of days - **Required**
- `--work-intensity`: Work intensity level (`light`, `medium`, `heavy`) - Default: `medium`
- `--extras`: Include optional extra items
- `--format`: Output format (`text`, `json`) - Default: `text`
- `--export`: Export as Markdown to specified filename

## Features

- ✅ Smart recommendations based on trip parameters
- ✅ Modular organization mapping
- ✅ FIKA CARRY product integration
- ✅ Markdown export for printable checklists
- ✅ JSON output for integration with other tools
- ✅ Calculates optimal clothing quantities
- ✅ Work gear recommendations by intensity

## Example Output

🎒 DIGITAL NOMAD PACKING LIST

📋 Trip Details: Type: WEEKEND Duration: 3 day(s) Work Intensity: MEDIUM Generated: 2024-01-15 10:30:00

🎒 Recommended Base Pack: Week Go 16L/22L (16L-22L) https://fikacarry.com/products/week-go-16l-22l

📦 Required Modules: ✓ CoilCrate Case ✓ KeyBit Pouch ✓ PackLite Combo Flat 4P ✓ DripDry Case