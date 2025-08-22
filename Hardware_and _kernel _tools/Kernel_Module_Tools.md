# Kernel Module Tools

## Description:

## Table of Contents

- `lsmod`
- `modinfo`
- `modprobe`

# Command: lsmod (List Modules)

## Description: Displays information on the currently loaded kernel modules on a Linux system

## Syntax

- `lsmod`

### Options

- `No flags or options`

# Command: modinfo

## Description: Lists detailed information about a given Linux kernel module

## Syntax

- `modinfo [Options] [module_file] | module_name`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-a` | Shows author of the module | `modinfo -a i915` |
| `-d` | Show description | `modinfo -d e1000e` |
| `-l` | Show license type | `modinfo -l snd_hda_intel` |
| `-p` | Show parameters the module accepts | `modinfo -p snd_hda_intel` |
| `-n` | Show the filename of the module | `modinfo -n i915` |
| `-F<field> | Displays only a specific field | `modinfo -F license i915` |
| `-k<kernel>` | Query module info for a specific kernel version | `modinfo -k 6.8.0-31-generic i915` |
| `-O` | Seperate output fields with NUL instead of newline | `modinfo -O i915` |

### Examples

### Retrieve information about a module by name

```bash
modinfo i915
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `modinfo` | Kernel command |
| `i915` | Target module |

# Command: modprobe

## Description: Used to add or remove kernel modules intelligently

