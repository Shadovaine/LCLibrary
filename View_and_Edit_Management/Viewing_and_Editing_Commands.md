# File Viewing and Editing

## Description: Commands used to see and/or modify files

## Table of Contents

- `cat`
- `less`
- `more`
- `head`
- `tail`
- `fold`
- `tac`
- `strings`
- `od`
- `xxd`
- `vipe`




# Command: Cat

## Syntax

- `cat [option] [ file….]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-A` | Shows all characters tabs, line ends, non-printing char | `cat -A secretfile` |
| `-b` | Numbers non-blank lines | `cat -b story.txt` |
| `-e` | Show $ at line ends and non-printing characters | `cat -e quote.txt` |
| `-E` | Show $ at end of each line | `cat -E poem.txt` |
| `-n` | Number all lines | `cat -n code.py` |
| `-s` | Squeeze multiple blank lines into one | `cat -s journal.txt` |
| `-T` | Show tabs as ^I | `cat -T notes.txt` |
| `-v` | Show non-printing characters | `cat -v dumpfile.txt` |

### Examples

### Number all lines

```bash
cat -n script.sh
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `cat` | Viewer command |
| `-n` | Directs to number lines |
| `script.sh` | Target file |

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
d
# Command: tac 

## Description: Reads a file from bottom to top line by line

## Syntax

- `tac [Option]...[File]...`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-b` | Attach the separator before instead of after | `tac -b data.txt` |
| `-r` | Treat the separator as a regex | `tac -r -s [0-9]{4}-' logs.txt` | 
| `-s<separator>` | Use a custom separator instead of newline | `tac -s ":" /etc/passwd` |

### Examples

### Reverse a file line-by-line

```bash
tac notes.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `tac` | Viewer command |
| `notes.txt` | Target file |

# Command: strings

## Description: Extracts and prints human-readable strings from binary files or blobs of data

## Syntax

- `strings [Options] file`

### Options

| Options | D*escriptions | Examples |
|---------|--------------|----------|
| `-a` | Scan entire file | `strings -a malware.exe` |
| `-n<numbers>--bytes=<number>` | Minimum string length to print | `strings -n 5 binary.dump` |
| `-t <radix>` | Print offset of string in file | `strings -t x /bin/ls` |
| `-e <encoding>` | Character encoding | `strings -e 1 firmaware.bin` |
| `-f` | Show the file name before each string | `strings -e 1 firmware.bin` |
| `-o` | Legacy: same as -t d -- show decimal offset | `strings -f *.o` |
| `-T<encoding>` | Specify encoding for output terminal | `strings -T UTF-8 core.dump` |

### Examples

### Scan a binary and show readable text

```bash
strings /usr/bin/whoami
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `strings` | Decoder command |
| `/usr/bin/whoami` | Target file to decode |

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

### od Output Formats

| od Formats | Descriptions |
|------------|--------------|
| `x1, x2` | Hex 1 or 2byte grouplings |
| `u1, u2, u4` | Unsigned ints |
| `d2, d4` | signed decimals |
| `f4, f8` | floating point |

### Examples 

### Dump stdin as hex

```bash
cat | od -tx1
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `cat` | viewing command |
| `od` | Dumping command |
| `-tx1` | Specifies output format |

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
