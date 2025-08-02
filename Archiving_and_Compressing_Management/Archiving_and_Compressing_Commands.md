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


## ** Command: tar 
**Description:** Archives multiple files into on file.

## **Syntax**
tar [OPTIONS] [ARCHIVE_FILE] [FILES/DIRS...]

### **Options**
- `-c`:	Create a new archive.
- `-x`:	Extract files from an archive.
- `-t`:	List archive contents.
- `-v`:	Verbose (show progress).
- `-f`: FILE	Use archive file FILE.
- `-z`:	Compress archive with gzip.
- `-j`:	Compress archive with bzip2.
- `-J`:	Compress archive with xz.

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

- **Create a gzip-compressed archive:**

```bash
tar -czvf backup.tar.gz /home/sue
```

- **List contents of an archive:**

```bash
tar -tvf backup.tar.gz
```

- **Extract an archive:**
```bash
tar -xvf backup.tar
```

- **Extract to a specific directory:**

```bash
tar -xvf backup.tar -C /tmp
```


## **gzip**
- Compresses files
- Alias for gunzip

## **Syntax**
- gzip [OPTIONS] FILE

### **Options**
- `-k`:	Keep original file.
- `-r`:	Compress files in directories recursively.
- `-d`:	Decompress files.
- `-c`: Write output to `stdout`
- `-f`: Force compression even if the file has multiple links or already exists.
- `-l`: List information about the compressed file.
- `-t`: Test the integrity of a compressed file
- `-v`: Verbose mode
- `-q`: Quiet mode
- `-#`: Set compression level ( 1 is the fastest/least compressed and 9 is slowest/most compressed).

### **Examples**
- __Compress a file:__
- `gzip file.txt`

- __Compress but keep original:__
- `gzip -k file.txt`

- __Decompress with gzip:__
- `gzip -d file.txt.gz`


## **gunzip**
- Decompresses .gz files.

## **Syntax**
- gunzip [OPTIONS] FILE.gz

### **Options**
- `-k`:  Keep the original `.gz` file after decompression
- `-c`:  Write output to `stdout` instead of creating a file
- `-f`:  Force decompression (overwrites existing files without prompting).
- `-l`:  Lit information about the compressed file (size, compression ratio).
- `-t`:  Test the integrity of a compressed file without extraction.
- `-v`:  Verbose mode
- `-q`:  Quiet mode

### **Examples**
-__Decompress a file:__
- `gunzip file.txt.gz`

- __Keep compressed file after decompressing:__
- `gunzip -k file.txt.gz`


## **zip**
- Compresses files into .zip archives.

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

### **Example**
- __Create a zip archive:__
- `zip archive.zip file1.txt file2.txt`

- __Zip a directory:__
- `zip -r archive.zip /home/sue`

- __Create password-protected zip:__
- `zip -e archive.zip secret.txt`


## **unzip**
- Extracts .zip archives.

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

### **Example**
-__Extract a zip archive:__
- `unzip archive.zip`

 -__Extract to a directory:__
- `unzip archive.zip -d /tmp`

- __List archive contents:__
- `unzip -l archive.zip`


## **bzip2**
- Compresses files using bzip2 algorithm.
- Alias for bunzip2
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
   
### **Example**
- __Compress a file:__
- `bzip2 file.txt`

- __Decompress:__
- `bzip2 -d file.txt.bz2`

- __Keep original file:__
- `bzip2 -k file.txt`


## **xz**
- Compresses files using xz algorithm (high compression).

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
- __Compress a file:__
- `xz file.txt`

- __Decompress:__
- `xz -d file.txt.xz`

- __Keep original file:__
- `xz -k file.txt`

