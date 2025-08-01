# **File Viewing and Editing**

## **Cat**

## **Syntax**
- cat [option] [ file….]

### **Options**
-n     Numbers all output lines
-b.    Number only non-blank lines
-s.    Suppress repeated blank lines ( squeeze  them)
-E.    Show $ at end of each line
-T.    Show tabs as ^I ( useful for debugging whitespace)


## **Less**
- allows u to view large files one page at a time

## **Syntax**
- less [OPTIONS] [FILE]

### **Options**
-N	Show line numbers.
-S	Disable line wrapping (long lines cut off).
+F	Open in “follow mode” (like tail -f).

#### **Examples**
- less /var/log/syslog


## **More**
- like less but can only scroll forward

## **Syntax**
- more [OPTIONS] [FILE]

### **Options**
- +n	Start at line n.
- /pattern	Search forward for “pattern”.

#### **Examples**
- more /etc/services
 - view a file
-more +20 bigfile.txt
- start viewing from line 20


## **Head**
- outputs the first few lines of a file, by default it spits out the first 10 lines

## **Syntax**
- head [OPTIONS] [FILE]

### **Options**
-n NUM	Show first NUM lines.
-c NUM	Show first NUM bytes (not lines).

## **Examples**
- head /etc/passwd
- show the first 10 lines
- head -n 5 myfile.txt
- show the first 5 lines


## **tail**
- outputs the last few lines of a file. Spits out the last 10 lines by default.

## **Syntax**
-tail [OPTIONS] [FILE]

### **Options**
-n NUM	Show last NUM lines.
-f	“Follow” the file as it grows.
-c NUM	Show last NUM bytes.

#### **Examples**
-tail /etc/passwd
- shows the last 10 lines
-tail -n 20 mylog.log
- shows the last 20 lines


## **fold**
- Wraps long lines so they fit in ur terminal

## **Syntax**
-fold [OPTIONS] [FILE]

### **Options**
-w NUM	Set line width to NUM characters.
-s	Break lines at spaces instead of cutting words.

#### **Wxamples**
- Wrap lines at 40 characters:
- fold -w 40 longfile.txt
- Wrap lines but don’t split words:
- fold -s -w 40 longfile.txt

## **stat – Detailed file information**

## **Syntax**
-stat [file]

### **Examples**
- stat /etc/passwd


## **Pro Tip**

- You can chain these together with pipes (|):

- View only the first 20 lines of a huge file:

- cat bigfile.txt | head -n 20

- View a growing log file in real-time:

- tail -f /var/log/syslog | grep "error"


