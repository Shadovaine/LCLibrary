# Archiving and Compressing Management

## Description: Commands used to create, extract, and manage archive files.

## Table of Contents

- `tar`
- `gzip`
- `gunzip`
- `zip`
- `unzip`
- `bzip2`
- `xz`
- `unp`

## Command: tar 

## Description: Archives multiple files into on file

## Syntax

tar `[OPTIONS] [ARCHIVE_FILE] [FILES/DIRS...]`

### Options

| Option | Description | Example |
|--------|-------------|---------|
| `-c` |	Create a new archive. | `tar -cf backup.tar /home/original` |
| `-x` | Extract files from an archive. | `tar -xf backup.tar` |
| `-t` | List archive contents. | `tar -tf backup.tar` |
| `-v` | Verbose mode. | `tar -vf backup.tar` |
| `-f` | FILE Use archive file. | `tar -f backup.tar` |
| `-z` | Compress archive with gzip. | `tar -xzf backup.tar.gz |
| `-j` | Compress archive with bzip2. | `tar -xjf backup.tar.bz2` |
| `-J` | Compress archive with xz. | `tar -xJf backup.tar.xz` |
| `-p` | Preserve file permissions. | `tar -cxpf backup.tar |
| `--same-owner` | Preserve original file ownership. | `tar -xzf backup.tar.gz --same-owner -C / |
| `-C` | Change to a specific directory before extracting. | `tar -xzf backup.tar.gz --same-owner -C / |
| `-A` | Append tar files to an existing archive. | `tar -Af backup.tar original.tar` |
| `-r` | Append files to the end of an archive. | `tar -rf backup.tar original.tar` |
| `-u` | Append only files that area newer than what is in the archive. | `tar -cuf backup.tar original.tar |
| `--remove-files` | Remove files after adding them to the archive. | `tar --remove-files -cf backup.tar original1.txt original2.txt` |
| `--exclude=PATTERN` | Exclude files matching a pattern. | `tar -czf backup.tar.gz --exclude=secret.txt original/ |
| `--wildcards` | Enable wildcard matching for patterns. | `tar -xzf backup.tar.gz --wildcards `*.log` |
| `--overwrite` | Overwrite existing file during extraction. | `tar -xvf backup.tar --overwrite` |
| `--strip-components=N` | Remove the firest N directory components when extracting. | 
| `-k` | Do not overwrite existing files when extracting. | `tar -xf backup.tar --strip-component-1` |
| `-lzma` | LZMA compression. | `tar --lzma -xvf backup.tar.lzma` |
  
### Extensions

| Extension | Description | Speed |
|-----------|-------------|-------|
| `.tar` | Raw tar achive with no compression. | Fastest | 
| `.tar.gz`or`.tgz` | A tar archive compressed with `gzip`. | Fast | 
| `.tar.bz2` | Compressed with `bzip2`. | Medium | 
| `.tar.xz` | Compressed with `xz`. | Slow | 
| `.tar.zst` | Compressed with `zstd`. | Very Fast | 

### Examples

### Create an archive

```bash
tar -cvf backup.tar /home/sue
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `tar` | Archive Command |
| `-c` | Create a new archive |
| `-v` | Verbose Mode |
| `-f` | Directs source FILE to use archive FILE. |
| `backup.tar` | Name of archive file. |
| `/home/sue` | Source file/directory to be archived. |

### Create a gzip-compressed archive

```bash
tar -czvf backup.tar.gz /home/sue
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `tar` | Archive Command. |
| `-c` | Says to create a new archive. |
| `-z` | Compress file using gzip. |
| `-v` | Verbose mode. |
| `-f` | Directs source FILE to use archive FILE. |
| `backup.tar.gz`| Name of archive file. |
| `/home/sue` | Source file/directory to be archived. |

### List contents of an archive

```bash
tar -tvf backup.tar.gz
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `tar` | Archive Command. |
| `-t` | List archive contents. |
| `-v` | Verbose mode. |
| `-f` | Directs source FILE to use archive FILE. |
| `backup.tar.gz` | Name of archived file to list. |

### Extract an archive

```bash
tar -xvf backup.tar
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `tar` | Archive Command. |
| `-x` | Extracts contents from an archive file. |
| `-v` | Verbose mode. |
| `-f` | Directs source FILE to use archive FILE. |
| `backup.tar` | Archived file to extract. |

### Extract to a specific directory

```bash
tar -xvf backup.tar -C /tmp
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `tar` | Archive Command. |
| `-x`| Extracts contents from an archive file. |
| `-v` | Verbose mode. |
| `-f` |  Directs source FILE to use archive FILE. |
| `backup.tar` | Archived file. |
| `-C` | Directs to extract to a specific location. |
| `/tmp` | Target location. |

  
# Command: gzip

## Description: Compresses files and is an alias for gunzip

## Syntax

- `gzip [OPTIONS] FILE`

### Options

| Options | Description | Example |
|---------|-------------|---------|
| `-k` | Keep original file. | `gzip -k file.txt` |
| `-r` | Compress files in directories recursively | `gzip -r /tmp/files` |
| `-d` | Decompress `.gz` files. | `gzip -d files.gz` |
| `-c` | Write output to `stdout`. | `gzip -c files.txt` |
| `-f` | Force compression even if the file has multiple links or already exists | `gzip -f files.txt` |
| `-l` | List information about the compressed file | `gzip -l files.gz` |
| `-t` | Test the integrity of a compressed file. | `gzip -t files.gz` |
| `-v` | Verbose mode. | `gzip -v files.gz` |
| `-q` | Quiet mode. | `gzip -q files.gz` |
| `-s` | Use a custom file extension instead of `.gz`. | `gzip -s files.txt` |
| `-#` | Set compression level ( 1 is the fastest/least compressed and 9 is slowest/most compressed). | `gzip -1 files.txt` |

### Examples

### Compress a file

```bash
gzip file.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `gzip` | File Compression Command. |
| `file.txt` | File to be compressed. |

### Compress but keep original

```bash
gzip -k file.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `gzip` | File Compression Command. |
| `-k` | Keep original file. |
| `file.txt` | File to be compressed. |
  
### Decompress with gzip

```bash
gzip -d file.txt.gz
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `gzip` | File Compression Command. |
| `-d` | Directs to Decompress a `.gz` file. |
| `file.txt.gz` | File to decompress. |

  
## Command: gunzip

## Description: Decompresses .gz files and is an alias for gzip

## Syntax

- `gunzip [OPTIONS] FILE.gz`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-k` | Keep the original `.gz` file after decompression. | `gunzip -k file.txt.gz` |
| `-c` | Write output to `stdout` instead of creating a file. | `gunzip -c file.txt.gz` |
| `-f` | Force decompression (overwrites existing files without prompting). | `gunzip -f file.txt.gz` |
| `-l` | Lit information about the compressed file (size, compression ratio). | `gunzip -l file.txt.gz` |
| `-t` | Test the integrity of a compressed file without extraction. | `gunzip -l file.txt.gz` |
| `-v` | Verbose mode. | `gunzip -v file.txt.gz` |
| `-q` | Quiet mode. | `gunzip -q file.txt.gz` |
| `-s` | Use a custom suffix for compressed/decompressed files. | `gunzip -s file.txt.gz` |
| `-d` | Decompress (for gzip, but default for gunzip). | `gunzip -d file.txt.gz` |

### Examples

### Decompress a file

```bash
gunzip file.txt.gz
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `gunzip` | Decompression Command. |
| `file.txt.gz` | Archived File to Decompress. |
  
### Keep compressed file after decompressing

```bash
gunzip -k file.txt.gz
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `gunzip` | Decompression Command. |
| `-k` | Directs to keep the original file. |
| `file.txt.gz` | Target file. |
  
## Command: zip

## Description: Compresses files into .zip archives

## Syntax

- `zip [OPTIONS] ARCHIVE_NAME.zip FILES...`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-r` | Include directories recursively. | `zip -r project.zip project/` |
| `-e` | Encrypt the archive (with password). | `zip -e project.zip project/` |
| `-q` | Quiet mode. | `zip -qre project.zip project/` |
| `-v` | Verbose mode. | `zip -v project.zip project/` |
| `-9` | Maximum compression. | `zip -r9 backup.zip project/` |
| `-0` | No compression. | `zip -r0 backup.zip project/` |
| `-u` | Update existing zip file. | `zip -u backup.zip project/` |
| `-d` | Delete file from an existing zip archive. | `zip -d backup.zip oldbackup.txt` |
| `-j` | Store files without directory paths. | `zip -j backup.zip project/` |
| `-x` | Exclude specific files or patterns. | `zip -x backup.zip project/` |
| `-i` | Include only the specified file or patterns. | `zip -i backup.zip project/` |
| `-n` | Do not compress files with certain suffixes. | `zip -n backup.zip project/` |
| `-m` | Move files into the archive. | `zip -m backup.zip file1.txt file2.txt` |

### Example

### Create a zip archive

```bash
zip archive.zip file1.txt file2.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `zip` | Compression Command. |
| `archive.zip` | Target archive file. |
| `file1.txt file2.txt` | Files to be compressed. |
  
### Zip a directory

```bash
zip -r archive.zip /home/sue
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `zip` | Compression Command. |
| `-r` | Directs to include directories recursively. |
| `archive.zip` | Target archive file. |
| `/home/sue` | Directory to compress. |
  
### Create password-protected zip

```bash  
zip -e archive.zip secret.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `zip` | Commpression Command. |
| `-e` | Encrypts compressed file. |
| `archive.zip` | Target archive file. |
| `secrect.txt` | Source file to be password-protected when compressed. |
  
# Command: unzip

## Description: Extracts .zip archives

## Syntax

- `unzip [OPTIONS] ARCHIVE_NAME.zip`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-l` | List contents of the zip file. | `unzip -l archive.zip` |
| `-d<DIR>` | Extract to a specific directory. | `unzip -d /tmp/extract archive.zip` |
| `-v` | Verbose mode. | `unzip -v archive.zip` |
| `-t` | Test the integrity of the zip file without extraction | `unzip -t archive.zip` |
| `-q` | Quiet mode. | `unzip -q archive.zip` |
| `-n` | Never overwrite existing files (skip duplicates) | `unzip -n archive.zip` |
| `-j` | Junk paths (ignore folder structure inside the archive, extract all files into the current directory) | `unzip -j archive.zip` |
| `-x <file>` | Exclude specific file from being extracted | `unzip -x "*.log" archive.zip` | 
| `-aa`| Convert text files to Unix line endings | `unzip -aa archive.zip` |
| `-u` | Treat achrive file names as UTF-8 (fixes encoding issues) | `unzip -u archive.zip` |
| `-p` | Extract files to `stdout` | `unzip -p archive.zip` |
| `-z` | Display the archive comment | `unzip -z archive.zip` |
| `-o` | Overwrite files automatically without prompting | `unzip -o archive.zip` |

### Example

### Extract a zip archive

```bash  
unzip archive.zip
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `unzip` | Extraction Command. |
| `archive.zip` | Target file to be extracted. |

### Extract to a directory

```bash
unzip archive.zip -d /tmp
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `unzip` | Extraction command. |
| `archive.zip` | Target archive file. |
| `-d` | Directs extractiong to a specific directory. |
| `/tmp` | Specific location for extaction. |
  
### List archive contents

```bash  
unzip -l archive.zip
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `unzip` | Extraction command. |
| `-l` | List contents of file. |
| `archive.zip` | Target location. |

# Command: bzip2

## Description: Compresses files and is an alias for bunzip2

## Syntax

- `bzip2 [OPTIONS] FILE`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-k` | Keep original file. | `bzip2 -k file.bz2` |
| `-d` | Decompress. | `bzip2 -d file.bz2` |
| `-f` | Force overwrite if the output file already exists. | `bzip2 -f file.bz2` |
| `-t` | Test the integrity of a compressed file. | `bzip2 -t file.bz2` |
| `-v` | Verbose mode. | `bzip2 -v file.bz2` |
| `-q` | Quiet mode. | `bzip2 -q file.bz2` |
| `-1` to `9` | Sets compression level. | `bzip2 -k9 file.bz2` |
| `-c` | Write output to `stdout`. | `bzip2 -c file.txt > file2.txt.bz2` |
| `-repretitive-best` | Optimize for files with many repeated sequences. | `bzip2 --repetitive-best bigfile.log` |
| `-z` | Force compression. | `bzip2 -z file.txt.bz2` |
| `-s` | Reduce memory usage. | `bzip2 -s file.txt.bz2` |

### Example

### Compress a file

```bash
bzip2 file.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `bzip2` | Compression Command. |
| `file.txt` | Target file. |
  
### Decompress

```bash  
bzip2 -d file.txt.bz2
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `bzip2` | Compression Command. |
| `-d` | Directs to decompress file. |
| `file.txt.bz2` | Target file. |
  
### Keep original file

```bash  
bzip2 -k file.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `bzip2` | Compression Command. |
| `-k` | Directs to keep original file. |
| `file.txt` | Target file. |
  
# Command: xz

## Description: Compresses files

## Syntax

- `xz [OPTIONS] FILE`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-k` | Keep original file. | ` xz -k backup.txt` |
| `-d` | Decompress a file. | ` xz -d backup.txt` |
| `-f` | Force overwrite if the output file already exists. | `xz -f backup.txt` |
| `-t` | Test the integrity of a compressed file. | `xz -t backup.txt` |
| `-v` | Verbose mode. | `xz -v backup.txt` |
| `-q` | Quiet mode. | `xz -q backup.txt` |
| `-1` to `-9` | Set compression level. | `xz -k9 backup.txt.xz` |
| `-c` | Write output to `stdout`. | `xz -c backup-txt > archive.xz` |
| `--threads=NUM` | Use multithreading to speed up compression or decompression. | `xz --threads=4 backup.iso` |
| `--single-stream` | Decompress only the first stream in a multi-stream `.xz` file. | `xz --single-stream backup.xz` |

### Examples

### Compress a file

```bash  
xz file.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `xz` | Compression Command. |
| `file.txt` | Target file. |
  
### Decompress

```bash  
xz -d file.txt.xz
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `xz` | Compression Command. |
| `-d` | Directs to decompress file. |
| `file.txt.xz` | Target file. |

### Keep original file

```bash  
xz -k file.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `xz` | Compression Command. |
| `-k` | Directs to keep original file. |
| `file.txt` | Target File. |
| `-k` | Directs to keep original file. |
| `file.txt` | Target file. |

# Command: unp 

## Description: Smart extractor for multiple compressed file formats. Supported formats: .zip, .tar, .gz, .bz2, .7z, .rar, etc

## Syntax

- `unp [Options] [archive1] [archive2...]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-v` | Verbose mode | `unp -v archive.tar.gz` |
| `-o<dir>` | Extract files into a specific output directory | `unp -o /tmp/myextract archive.zip` |
| `-d` | Delete archive after successful extraction | `unp -d file.tar.gz` |
| `-u` | Update/skip existing files instead of overwriting them | `unp -u data.zip` |
| `-n` | Do not overwrite existing files | `unp -n mybackup.tar.gz` |
| `-q` | quiet mode | `unp -q archive.zip` |
| `-t` | test archive without extracting | `unp -t archive.7z |
| `-e` | Expand archive recursively | `unp -e nested.tar.gz` |

### Examples

### Delete archive after successfully extracting items

```bash
unp -d secrets.tar.gz
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `unp` | Archive command| 
| `-d` | Directs to delete archive after extraction |
| `secrets.tar.gz` | Target archive file |