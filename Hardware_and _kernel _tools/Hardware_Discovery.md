# Hardware Discovery

## Description:

## Tables of Contents

- `lspci`
- `lsusb`
- `sensors`
- `hwinfo`

# Command: lspci

## Description: Lists all PCI (Perioheral Component Interconnect) buses and the devices connected to them

## Syntax

- `lspci [Options]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-v` | Verbose mode | `lspci -v` |
| `-vv` | Extra Verbose Mode | `lspci -vv` |
| `-n` | Shows numeric IDs instead of text | `lspci -n` |
| `-nn` | Both numeric and human readable form | 'lspci -nn` |
| `-xxx` | Detailed dump of config space | `lspci -xxx` |
| `-k` | Show kernel driver in use | `lspci -k` |
| `-mm` | Show machine-readable/ scripting format | `lspci -mm` |
| `-t` | Tree view | `lspci -t` |