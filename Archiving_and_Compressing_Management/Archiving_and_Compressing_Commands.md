# **Archiving and Compressing Management**

## **tar -Tape Archive**
- Used to create, extract, and manage archive files (commonly .tar, .tar.gz, .tar.bz2).
- Common extensions *.tar,*.tar.gz, *.tar.bz2

- **Syntax**
tar [OPTIONS] [ARCHIVE_FILE] [FILES/DIRS...]

### **Options**
-c	Create a new archive.
-x	Extract files from an archive.
-t	List archive contents.
-v	Verbose (show progress).
-f FILE	Use archive file FILE.
-z	Compress archive with gzip.
-j	Compress archive with bzip2.
-J	Compress archive with xz.

#### **Example**

Create an archive:
tar -cvf backup.tar /home/jake

Create a gzip-compressed archive:
tar -czvf backup.tar.gz /home/jake

List contents of an archive:
tar -tvf backup.tar.gz

Extract an archive:
tar -xvf backup.tar

Extract to a specific directory:
tar -xvf backup.tar -C /tmp

## **gzip**
- Compresses files using gzip algorithm.

## **Syntax**
- gzip [OPTIONS] FILE

### **Options**
-k	Keep original file.
-r	Compress files in directories recursively.
-d	Decompress files (alias for gunzip).

#### **Example**
Compress a file:
gzip file.txt

Compress but keep original:
gzip -k file.txt

Decompress with gzip:
gzip -d file.txt.gz


## **gunzip**
- Decompresses .gz files.

## **Syntax**
- gunzip [OPTIONS] FILE.gz

### **Example**

Decompress a file:
gunzip file.txt.gz

(Restores: file.txt)

Keep compressed file after decompressing:
gunzip -k file.txt.gz


## **zip**
- Compresses files into .zip archives.

## **Syntax**
zip [OPTIONS] ARCHIVE_NAME.zip FILES...

### **Options**
-r	Include directories recursively.
-e	Encrypt the archive (with password).

#### **Example**

Create a zip archive:
zip archive.zip file1.txt file2.txt

Zip a directory:
zip -r archive.zip /home/jake

Create password-protected zip:
zip -e archive.zip secret.txt

## **unzip**
- Extracts .zip archives.

## **Syntax**
- unzip [OPTIONS] ARCHIVE_NAME.zip

### **Options**
-l	List contents of the zip file.
-d DIR	Extract to a specific directory.

#### **Example**

 Extract a zip archive:
unzip archive.zip

 Extract to a directory:
unzip archive.zip -d /tmp

 List archive contents:
unzip -l archive.zip


## **bzip2**
- Compresses files using bzip2 algorithm.

## **Syntax**
- bzip2 [OPTIONS] FILE

### **Options**
-k	Keep original file.
-d	Decompress (alias for bunzip2).

#### **Example**

Compress a file:
bzip2 file.txt
(Output: file.txt.bz2)

Decompress:
bzip2 -d file.txt.bz2

Keep original file:
bzip2 -k file.txt

## **xz**
- Compresses files using xz algorithm (high compression).

## **Syntax**
- xz [OPTIONS] FILE

### **Options**
-k	Keep original file.
-d	Decompress.

#### **Examples**

Compress a file:
xz file.txt
(Output: file.txt.xz)

Decompress:
xz -d file.txt.xz

Keep original file:
xz -k file.txt

