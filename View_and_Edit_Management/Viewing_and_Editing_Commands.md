# File Viewing and Editing

## Description: Commands used to see and/or modify files

## Table of Contents

- `cat`
- `less`
- `more`
- `head`
- `tail`
- `fold`
- `stat`
- `tac`
- `strings`
- `od`
- `xxd`
- `vipe`




# Command: Cat

## Syntax

- `cat [option] [ file….]`

### Options

-n     Numbers all output lines
-b.    Number only non-blank lines
-s.    Suppress repeated blank lines ( squeeze  them)
-E.    Show $ at end of each line
-T.    Show tabs as ^I ( useful for debugging whitespace)

### Examples

# Command: Less

## Description: Allows u to view large files one page at a time

## Syntax

- `less [OPTIONS] [FILE]`

### Options

-N	Show line numbers.
-S	Disable line wrapping (long lines cut off).
+F	Open in “follow mode” (like tail -f).

### Examples

- less /var/log/syslog

# Command: More

## Description: Similar to less but can only scroll forward

## Syntax

- `more [OPTIONS] [FILE]`

### Options

- +n	Start at line n.
- /pattern	Search forward for “pattern”.

### Examples

### view a file

more /etc/services

### start viewing from line 20

more +20 bigfile.txt

# Command: Head

## Description: outputs the first few lines of a file, by default it spits out the first 10 lines

## Syntax

- `head [OPTIONS] [FILE]`

### Options

-n NUM	Show first NUM lines.
-c NUM	Show first NUM bytes (not lines).

### Examples

### Show the first 10 lines

head /etc/passwd

### Show the first 5 lines

head -n 5 myfile.txt

# Command: tail

## Description: outputs the last few lines of a file. Spits out the last 10 lines by default

## Syntax

- `tail [OPTIONS] [FILE]`

### Options

-n NUM	Show last NUM lines.
-f	“Follow” the file as it grows.
-c NUM	Show last NUM bytes.

### Examples

### Shows the last 10 lines

tail /etc/passwd
### Shows the last 20 lines

tail -n 20 mylog.log

# Command: fold

## Description: Wraps long lines so they fit in ur terminal

## Syntax

- `fold [OPTIONS] [FILE]`

### Options

-w NUM	Set line width to NUM characters.
-s	Break lines at spaces instead of cutting words.

### Examples

### Wrap lines at 40 characters

fold -w 40 longfile.txt

### Wrap lines but don’t split words

fold -s -w 40 longfile.txt

# Command: stat

## Description: Detailed file information**

## Syntax

-`stat [file]`

### Options

### Examples

- stat /etc/passwd

# Pro Tip and Examples

## You can chain these together with pipes (|)

## View only the first 20 lines of a huge file

cat bigfile.txt | head -n 20

## View a growing log file in real-time

tail -f /var/log/syslog | grep "error"

# Command: tac

## Description:

## Syntax

### Options

### Examples

# Command: strings

## Description:

## Syntax

### Options

### Examples

# Command: od

## Description: Stands for `octal dump`, it can display files in hex, binary, octal, ASCII, decimal, or all at once. Its a raw byte-level viewer for binary files.

## Syntax

- `od [Options] [File]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-o`or`(none)` | Shows octal bytes | `od` |
| `-x` | Hexadecimal output | `od -x myfile` |
| `-c` | Character dump (ASCiI) | `od -c myfile` |
| `-b` | Binary(octal) dump of bytes | `od -b myfile` |
| `-d` | Unsigned decimal format | `od -d myfile` |
| `-t` | Specify output format | `od -t x1 myfile` |
| `-N<num>` | Read only N bytes | `od -N 16 myfile` |
| `j<num>` | Skip N bytes before dumping | `od -j 16 -x myfile` |
| -v` | Do not suppress repeated lines | `od -v -x myfile` |

### 
### Examples 

# Command: xxd

## Description: Creates a hex dump of a given file, or STDIN, and can convert it back to binary if needed

## Syntax

- `xxd [Options] [file] [outfile]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-p` | Plain hexdump (no addresses, no ASCII) | `xxd -p myfile` |
| `-r` | Reverse operation (hex back to binary; essential to reverse a patch or decode raw hex data) | `xxd -r -p hexfile.txt > recovered.txt` |
| `-c<cols>` | Change number of bytes per line | `xxd -c 8 myfile` |
| `-g<bytes>` | Group bytes together | `xxd -g 2 myfile` |
| `-s<offset>` | Start at byte offset (can use hex) | `xxd -s 0x10 myfile` |
| `-l<length>` | Limit output to N bytes | `xxd -l 32 myfile` |
| `-u` | Uppercase hex | `xxd -u myfile` |
| `-i` | output as C-style include array | `xxd -i myfile` |
| `-e` | Little-endian hex dump (rarely used) | `xxd -e myfile` |

### Reverse a patch

### Step 1: Hexdump the binary

```bash
xxd -p original.bin > dump.hex
```

### Step 2: Edit the hex dump in a text editor

### Step 3: Convert back

```bash
xxd -r -p dump.hex > modified.bin
```

### Examples

### View a file as hex

```bash
xxd /bin/ls | less
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `xxd` | Hex command |
| `/bin/ls` | Target file to hexdump |
| `less` | Piped and less Directs to view hexdump |

### Dump first 64 bytes of a file

```bash
xxd -l 64 myfile
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `xxd` | Hex command |
| `-l 64` | Sets the length to be hexdumped to 64 bytes |
| `myfile` | Target file |

# Command: vipe

## Description: Edit stdin input in your $EDITOR (usually nano or vim). Acts as a pipe-based "pause and edit" tool. Use it in between pipes.

## Overall vipe process

- `It takes input from a command`
- `Opens a text editor`
- `then saves and exits to continue processing`

## Syntax

- `[command] vipe [command]`

### Options

- `No standard options`
- `User does need to set specific editor to have vipe use during session. It can be temporary or made permanent`

### Examples

### Edit output from `echo` before saving

```bash
echo "Name is learning Linux like a beast!" | vipe > notes.txt
```

### Interactive editing during a pipeline

```bash
cat /etc/passwd | vipe | grep bash
```
