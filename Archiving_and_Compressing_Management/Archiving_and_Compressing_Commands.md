# **Archiving and Compressing Management**

## **Commands used to create, extract, and manage archive files.**

## **Table of Contents**
- `tar`
- `gzip`
- `gunzip`
- `zip`
- `unzip`
- `bzip2`
- `xz`


## Command: tar 
**Description:** Archives multiple files into on file.

## **Syntax**
tar [OPTIONS] [ARCHIVE_FILE] [FILES/DIRS...]

### **Options**
- `-c`:	 Create a new archive.
- `-x`:	 Extract files from an archive.
- `-t`:	 List archive contents.
- `-v`:	 Verbose (show progress).
- `-f`:  FILE	Use archive file FILE.
- `-z`:	 Compress archive with gzip.
- `-j`:	 Compress archive with bzip2.
- `-J`:	 Compress archive with xz.
- `-p`:  Preserve file permissions.
- `--same-owner`:  Preserve original file ownership.
- `-C`:  Change to a specific directory before extracting.
- `-A`:  Append tar files to an existing archive.
- `-r`:  Append files to the end of an archive.
- `-u`:  Append only files that area newer than what is in the archive.
- `--remove-files`:  Remove files after adding them to the archive.
- `--exclude=PATTERN`:  Exclude files matching a pattern.
- `--wildcards`:  Enable wildcard matching for patterns.
- `--overwrite`:  Overwrite existing file during extraction.
- `--strip-components=N`:  Remove the firest N directory components when extracting
- `-k`:  Do not overwrite existing files when extracting.
- `-lzma`:  LZMA compression.
  
### **Extensions**
- `.tar`:  Raw tar achive with no compression. 
- **Fastest**
- `.tar.gz` or `.tgz`: A tar archive compressed with `gzip`. 
- **Fast**
- `.tar.bz2`: Compressed with `bzip2`. 
- **Medium**
- `.tar.xz`: Compressed with `xz`. 
- **Slow**
- `.tar.zst`:  Compressed with `zstd`. 
- **Very Fast**

### **Examples**
- **Create an archive:**

```bash
tar -cvf backup.tar /home/sue
```

### **Breakdown**
- `tar`:  Archive Command
- `-c`:  Create a new archive
- `-v`:  Verbose Mode
- `-f`:  Directs source FILE to use archive FILE
- `backup.tar`:  Name of archive file
- `/home/sue`:  Source file/directory to be archived.

- **Create a gzip-compressed archive:**

```bash
tar -czvf backup.tar.gz /home/sue
```

### **Breakdown**
- `tar`:  Archive Command
- `-c`:  Says to create a new archive
- `-z`:  Compress file using gzip.
- `-v`:  Verbose mode.
- `-f`:  Directs source FILE to use archive FILE.
- `backup.tar.gz`:  Name of archive file.
- `/home/sue`:  Source file/directory to be archived.

- **List contents of an archive:**

```bash
tar -tvf backup.tar.gz
```

### **Breakdown**
- `tar`:  Archive Command
- `-t`:  List archive contents.
- `-v`:  Verbose mode.
- `-f`:  Directs source FILE to use archive FILE.
- `backup.tar.gz`:  Name of archived file to list.

- **Extract an archive:**
```bash
tar -xvf backup.tar
```

### **Breakdown**
- `tar`:  Archive Command.
- `-x`:  Extracts contents from an archive file.
- `-v`:  Verbose mode.
- `-f`:  Directs source FILE to use archive FILE.
- `backup.tar`:  Archived file to extract.

- **Extract to a specific directory:**

```bash
tar -xvf backup.tar -C /tmp
```

### **Breakdown**
- `tar`:  Archive Command.
- `-x`:  Extracts contents from an archive file.
- `-v`:  Verbose mode.
- `-f`:  Directs source FILE to use archive FILE.
- `backup.tar`:  Archived file
- `-C`:  Directs to extract to a specific location
- `/tmp`:  Target location.

  
## Command: gzip
**Description:** Compresses files and is an alias for gunzip.

## **Syntax**
- gzip [OPTIONS] FILE

### **Options**
- `-k`:	 Keep original file.
- `-r`:	 Compress files in directories recursively.
- `-d`:	 Decompress `.gz` files.
- `-c`:  Write output to `stdout`
- `-f`:  Force compression even if the file has multiple links or already exists.
- `-l`:  List information about the compressed file.
- `-t`:  Test the integrity of a compressed file
- `-v`:  Verbose mode
- `-q`:  Quiet mode
- `-s`:  Use a custom file extension instead of `.gz`.
- `-#`:  Set compression level ( 1 is the fastest/least compressed and 9 is slowest/most compressed).

### **Examples**
- **Compress a file:**
  
```bash
gzip file.txt
```

### **Breakdown**
- `gzip`:  File Compression Command.
- `file.txt`:  file to be compressed.

- **Compress but keep original:**
  
```bash
gzip -k file.txt
```

### **Breakdown**
- `gzip`:  File Compression Command.
- `-k`:  Keep original file.
- `file.txt`:  file to be compressed.
  
- **Decompress with gzip:**
  
```bash
gzip -d file.txt.gz
```

### **Breakdown**
- `gzip`:  File Compression Command.
- `-d`:  Directs to Decompress a `.gz` file
- `file.txt.gz`:  File to decompress.

  
## Command: gunzip
**Description:** Decompresses .gz files and is an alias for gzip.

## **Syntax**
- gunzip [OPTIONS] FILE.gz

### **Options**
- `-k`:  Keep the original `.gz` file after decompression
- `-c`:  Write output to `stdout` instead of creating a file
- `-f`:  Force decompression (overwrites existing files without prompting).
- `-l`:  Lit information about the compressed file (size, compression ratio).
- `-t`:  Test the integrity of a compressed file without extraction.
- `-v`:  Verbose mode
- `-q`:  Quiet mode.
- `-s`:  Use a custom suffix for compressed/decompressed files.
- `-d`:  Decompress (for gzip, but default for gunzip).

### **Examples**
-**Decompress a file:**

```bash
gunzip file.txt.gz
```

### **Breakdown**
- `gunzip`:  Decompression Command.
- `file.txt.gz`:  Archived File to Decompress.
  
- **Keep compressed file after decompressing:**

```bash
gunzip -k file.txt.gz
```

### **Breakdown**
- `gunzip`:  Decompression Command.
- `-k`:  Directs to keep the original file.
- `file.txt.gz`:  Target file.
  

## Command: zip
**Description** Compresses files into .zip archives.

## **Syntax**
- zip [OPTIONS] ARCHIVE_NAME.zip FILES...

### **Options**
- `-r`:	 Include directories recursively.
- `-e`: 	Encrypt the archive (with password).
- `-q`:  Quiet mode
- `-v`:  Verbose mode
- `-9`:  Maximum compression
- `-0`:  No compression
- `-u`:  Update existing zip file
- `-d`:  Delete file from an existing zip archive.
- `-j`:  Store files without directory paths.
- `-x`:  Exclude specific files or patterns.
- `-i`:  Include only the specified file or patterns.
- `-n`:  Do not compress files with certain suffixes.
- `-m`:  Move files into the archive

### **Example**
- **Create a zip archive:**

```bash
zip archive.zip file1.txt file2.txt
```

### **Breakdown**
- `zip`:  Compression Command.
- `archive.zip`:  Target archive file.
- `file1.txt file2.txt`:  Files to be compressed.
  
- **Zip a directory:**

```bash
zip -r archive.zip /home/sue
```

### **Breakdown**
- `zip`:  Compression Command.
- `-r`:  Directs to include directories recursively.
- `archive.zip`:  Target archive file.
- `/home/sue`:  Directory to compress.
  
- **Create password-protected zip:**

```bash  
zip -e archive.zip secret.txt
```

### **Breakdown**
- `zip`:  Commpression Command.
- `-e`:  Encrypts compressed file.
- `archive.zip`:  Target archive file.
- `secrect.txt`:  Source file to be password-protected when compressed.
  
## Command: unzip
**Description** Extracts .zip archives.

## **Syntax**
- unzip [OPTIONS] ARCHIVE_NAME.zip

### **Options**
- `-l`:	 List contents of the zip file.
- `-d`:  DIR	Extract to a specific directory.
- `-v`:  Verbose mode
- `-t`:  Test the integrity of the zip file without extraction.
- `-q`:  Quiet mode
- `-n`:  Never overwrite existing files (skip duplicates).
- `-j`:  Junk paths (ignore folder structure inside the archive, extract all files into the current directory).
- `-x <file>`: Exclude specific file from being extracted.
- `-aa`:  Convert text files to Unix line endings.
- `-u`:  Treat achrive file names as UTF-8 (fixes encoding issues.)
- `-p`:  Extract files to `stdout`.
- `-z`:  Display the archive comment.
- `-o`:  Overwrite files automatically without prompting.

### **Example**
- **Extract a zip archive:**

```bash  
unzip archive.zip
```

### **Breakdown**
- `unzip`:  Extraction Command.
- `archive.zip`:  target file to be extracted.
    
 - **Extract to a directory:**

```bash
unzip archive.zip -d /tmp
```

### **Breakdown**
- `unzip`:  Extraction command.
- `archive.zip`:  Target archive file
- `-d`:  Directs extractiong to a specific directory.
- `/tmp`:  Specific location for extaction.
  
- **List archive contents:**

```bash  
unzip -l archive.zip
```
### **Breakdown**
- `unzip`:  Extraction command.
- `-l`:  List contents of file.
- `archive.zip`:  Target location.
  

## Command: bzip2
**Description** Compresses files and is an alias for bunzip2.

## **Syntax**
- bzip2 [OPTIONS] FILE

### **Options**
- `-k`:	 Keep original file.
- `-d`: 	Decompress.
- `-f`:  Force overwrite if the output file already exists.
- `-t`:  Test the integrity of a compressed file.
- `-v`:  Verbose mode
- `-q`:  Quiet mode
- `-1` to `9`: Sets compression level.
- `-c`:  Write output to `stdout`.
- `-repretitive-best`:  Optimize for files with many repeated sequences.
- `-z`:  Force compression.
- `-s`:  Reduce memory usage.
  
   
### **Example**
- **Compress a file:**

```bash
bzip2 file.txt
```

### **Breakdown**
- `bzip2`:  Compression Command.
- `file.txt`:  Target file.
  
- **Decompress:**

```bash  
bzip2 -d file.txt.bz2
```

### **Breakdown**
- `bzip2`:  Compression Command.
- `-d`:  Directs to decompress file.
- `file.txt.bz2`:  target file.
  
- **Keep original file:**

```bash  
bzip2 -k file.txt
```

### **Breakdown**
- `bzip2`:  Compression Command.
- `-k`:  Directs to keep original file.
- `file.txt`:  Target file.

  
## Command: xz
**Description** Compresses files.

## **Syntax**
- xz [OPTIONS] FILE

### **Options**
- `-k`:	 Keep original file.
- `-d`: 	Decompress a file.
- `-f`:  Force overwrite if the output file already exists.
- `-t`:  Test the integrity of a compressed file.
- `-v`:  Verbose mode
- `-q`:  Quiet mode
- `-1` to `-9`: Set compression level
- `-c`:  Write output to `stdout`.
- `--threads=NUM`:  Use multithreading to speed up compression or decompression.
- `--single-stream`:  Decompress only the first stream in a multi-stream `.xz` file.

### **Examples**
- **Compress a file:**

```bash  
xz file.txt
```

### **Breakdown**
- `xz`:  Compression Command.
- `file.txt`:  target file.
  
- **Decompress:**

```bash  
xz -d file.txt.xz
```

### **Breakdown**
- `xz`:  Compression Command.
- `-d`:  Directs to decompress file.
- `file.txt.xz`:  target file.
- **Keep original file:**

```bash  
xz -k file.txt
```

### **Breakdown**
- `xz`:  Compression Command.
- `-k`:  Directs to keep original file.
- `file.txt`:  target file.
