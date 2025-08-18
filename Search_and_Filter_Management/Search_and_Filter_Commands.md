# Search and Filter Management

## Description: Commands designed to find stuff within Linux

## Table of Contents

- `grep`
- `egrep`
- `fgrep`
- `cut`
- `sed`
- `awk`
- `sort`
- `uniq`

# Command: Grep

## Description: Classic text and content search command

## Syntax

- `grep [options] pattern [file…]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-i` | Case-insensitive search | `grep -i "error" logfile.txt` |
| `-c` | Count Matches | `grep -c "error" logfile.txt` |
| `-n` | Show the line numbers | `grep -n "error" logfile.txt` |
| `-v` | Invert Match | `grep -v "error" logfile.txt` |
| `-w` | Match whole words only | `grep -w "error" logfile.txt` |
| `-x` | Match whole lines only | `grep -x "error" logfile.txt` |
| `-r` or `-R` | Recursive search | `grep -r "error" /var/log/` |
| `-l` | Show only filenames with matches | `grep -l "error" *.log` |
| `-L` | Show only filenames without matches | `grep -L "error" *.log` |
| `-o` | Show match only | `grep -o "error" logfile.txt` |
| `-B` | Print n lines before match | `grep -B 3 "error" logfile.txt` |
| `-A` | Print n lines after match | `grep -A 3 "error" logfile.txt` |
| `-C` | Print n lines around match | `grep -C 3 "error" logfile.txt` |
| `-E` | Extended regex -E | `grep -E "error" logfile.txt |
| `-F` | Fixed string | `grep -F "a+b" logfile.txt` |
| `-h` | Suppress filename in output | `grep -h "error" *.log` |
| `-H` | Force filename output | `grep -H "error" logfile.txt` |
| `-q` | Quiet mode | `grep -q "error" logfile.txt && echo "Found!" |
| `-a` | Binary files search | `grep -a "password" core.dump` |
| `--exclude` | Exclude files | `grep -r "error" /var/log/ --exclude-dir="old"` |
| `--color` | color Matches | `grep --color=always "error" logfile.txt` |d

### Examples

```bash
grep -i "password" /etc/passwd
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `grep` | Search command |
| `-i` | Case-insensitive search |
| `"password"` | word to search for |
| `/etc/passwd` | file to search in |

# Command: egrep

## Description: Same as running `grep -E`, it enables Extended Regular Expression(ERE) by default

## Syntax

- `egrep [OPTIONS] PATTERN [FILE...]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-i` | Ignore case | `egrep -i "error/warning" logfile.txt` |
| `-v` | Invert match (show non-matching) | `egrep -v "DEBUG/TRACE" logfile.txt` |
| `-r` | Recursive search | `egrep -r "TODO/FIXME" /home/name/projects/` |
| `-c` | Count matches | `egrep -c "fail/error" logfile.txt` |
| `-n` | Show line numbers | `egrep -n "admin/root" /etc/passwd` |
| `-H` | Show filename in output | `egrep -H "main/function" *.c` |
| `-h` | Suppress filename in output | `egrep -h "password/key" *.conf` |
| `-l` | List with matches | `egrep -l "root/admin" /etc/` |
| `-o` | Show only the matching part | `egrep -o "[0-9][3]" data.txt` |
| `-q` | Quiet mode | `egrep -q "error" logfile.txt && echo "Found error"` |
| `-s` | Suppress error about missing files | `egrep -s "root" missinfile.txt` |
| `-w` | Match whole words only | `egrep -w "cat/dog" pets.txt` |
| `-x` | Match whole lines only | `egrep -x "hello/goobye" greeting.txt` |
| `-A<NUM>` | Print NUM lines after match` | `egrep -A 2 "error" logfile.txt` |
| `-B<NUM>` | Print NUM lines before match | `egrep -B 2 "error" logfile.txt` |
| `-C<NUM>` | Print NUM lines of context | `egrep -C 3 "error" logfile.txt` |
| `-m<NUM>` | Stop after NUM matches | `egrep -m 4 "error" logfile.txt` |
| `-r` or -R` | Recursive search in directories | `egrep -r "TODO/FIXME` | /home/name/projects/` |
| `-Z` or `--null` | Output filenames with NULL instead of newline | `egrep -Z "pattern" *.txt` |

### Examples

### Find lines with “error” or “fail”

```bash
egrep "error|fail" logfile.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `egrep` | Search command |
| `error/fail` | Pattern to search for |
| `logfile.txt` | Target file |

### Case-insensitive search

```bash
egrep -i "warning" logfile.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `egrep` | Search command
| `-i` | Ignore case |
| `warning` | Pattern to search for |
| `logfile.txt` | Target file |

### Recursive search for .conf files

```bash
egrep -r "Listen" /etc/apache2/
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `egrep` | Search command |
| `-r` | Recursive command |
| `Listen` | pattern to search for |
| `/etc/apache2/` | Target file |

# Command: fgrep

## Description: Searches for **literal text** not regex patterns, stands for Fixed-string Global Regular Expression Print

## Syntax

- `fgrep [OPTIONS] PATTERN [FILE...]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-i` | Ignore case | `fgrep -i "Error" logfile.txt` |
| `-c` | count matches | `fgrep -c "fail" logfile.txt` |
| `-n` | Show line numbers | `fgrep -n "root" /etc/passwd` |
| `-H` | Show filename in output | `fgrep -H "main *.c` |
| `-h` | Suppres filename in output | `fgrep -h " password" *.conf` |
| `-l` | List files with matches | `fgrep -l "root" /etc/*` |
| `-L` | List files without matches | `fgrep -L "root" /etc/*` |
| `-o` | Show only matching text | `fgrep -o "error" logfile.txt` |
| `-q` | quiet mode | `fgrep -q "error" logfile.txt && echo "found error"` |
| `-s` | Suppress error messages | `fgrep -s "root" missingfile.txt` |
| `-w` | Match whole words | `fgrep -w "cat" pets.txt` |
| `-x` | Match whole line | `fgrep -x " admin" users.txt` |
| `-A<NUM>` | Print NUM lines after match` | `fgrep -A 2 "error" logfile.txt` |
| `-B<NUM>` | Print NUM lines before match | `fgrep -B 2 "error" logfile.txt` |
| `-C<NUM>` | Print NUM lines of context | `fgrep -C 3 "error" logfile.txt` |
| `-m<NUM>` | Stop after NUM matches | `fgrep -m 4 "error" logfile.txt` |
| `-r` or -R` | Recursive search in directories | `fgrep -r "TODO/FIXME` |
| `-Z` or `--null` | Output filenames with NULL instead of newline | `fgrep -Z "pattern" *.txt |

### Examples

### Find exact string

```bash
fgrep "if [ $USER == root ]" script.sh
```

### Recursive literal search

```bash
fgrep -r "127.0.0.1" /etc/
```

# Command: cut

## Description: Extract sections of text by character position, byte position, and by fields using delimiters

## Syntax

- `cut [OPTIONS] [FILE...]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-b LIST` | Extract specific bytes from each line | `cut -b 1-3 file.txt` |
| `-c LIST` | Extract specific characters | `cut -c 1-3 file.txt` |
| `-f LIST` | Select fields | `cut -f 1,3 /etc/passwd` |
| `-d DELIM` | Specify field delimiter (default is tab) | `cut -d "," -f 2 file.csv` |
| `-s` | Suppress lines without delimiter | cut -d ":" -f 2 -s file.txt` |
| `--complement` | Invert selection | `cut -c 1-4 --complement file.txt` |
| `--output-delimiter=STR` | Change output delimiter | `cut -d ":" -f 1,2 --output delimiter=:` |

### Examples

### Get first 10 characters of each line

```bash
cut -c 1-10 file.txt
```

### Extract first column (fields delimited by)

```bash
cut -d ":" -f 1 /etc/passwd
```

### Combine with sort

```bash
cut -d ":" -f 1 /etc/passwd | sort
```

# Command: sed

## Description: Stream editor for text manipulation

## Syntax

- `sed [OPTIONS] 'SCRIPT' [FILE...]`

### Options

| Options | Descriptions | Examples | 
|---------|--------------|----------|
| `-n` | Only prints what you explicitly tell it to | `sed -n '2p' file.txt` |
| `-e` | Allows using more than one `sed` command | `sed -e 's/foo/bar/' -e 's/baz/qux/' file.txt` |
| `-f` | Use a script file with multiple `sed` instructions | sed -f script.sed file.txt` |
| `-i` | Overwrites the original file | `sed -i 's/cat/dog/g' pets.txt` |

### Commonly Used `sed` commands

| Common Commands | Description |
|-----------------|-------------|
| `s` | Replaces first occurrence of 'command' with second occurrence |
| `g` | Global Replacement - Replaces all occurrences with new occurrence |
| `d` | Delete specified amount of lines |
| `p` | Print specified amount of lines |
| `i` | Insert line before match |
| `a` | Append line after match | 
| `c` | Change lines |

### Examples

### Replace “foo” with “bar” globally

```bash
sed 's/foo/bar/g' file.txt
```

### Print lines 5–10

```bash
sed -n '5,10p' file.txt
```

### Delete comment lines starting with #

```bash
sed '/^#/d' file.txt
```

# Command: awk

## Description: Text processing and reporting

## Syntax

- `awk [OPTIONS] 'PATTERN { ACTION }' [FILE...]`

### Options

-F Set field separator (default: space).

### Examples

### Print first column

```bash
awk '{print $1}' file.txt
```

### Print usernames from passwd

```bash
awk -F: '{print $1}' /etc/passwd
```

### Print lines where field 3 > 1000

```bash
awk '$3 > 1000' /etc/passwd
```

# Command: sort

## Description: Sort text lines

## Syntax

- `sort [OPTIONS] [FILE]`

### Options

-r Reverse sort order.
-n Numeric sort.
-u Unique lines only (like uniq).
-k Sort by specific field/column.

### Examples

### Sort numerically on the second column

```bash
sort -n -k2 file.txt
```

# Command: uniq

## Description: Filter out repeated lines

## Syntax

- `uniq [OPTIONS] [INPUT [OUTPUT]]`

### Options

-c Prefix lines with counts.
-d Show only duplicate lines.
-u Show only unique lines.

### Examples

### Counts unique sorted lines

```bash
sort file.txt | uniq -c
```
