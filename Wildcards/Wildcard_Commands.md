# **Linux wildcards**

## ** * **
- matches zero or more characters in a file name

### **Examples**
ls *	List all files in the current directory.
rm *.txt	Delete all files ending with .txt.
cp /var/log/* backup/	Copy all files from /var/log to backup/.
Matches everything, except hidden files


## **?**
- Matches exactly one character

### **Examples**
ls file?.txt	Match file1.txt, fileA.txt, but not file10.txt.
mv ?.jpg images/	Move all .jpg files with one character filenames into images/.
Each ? Represents one single character


## **[]**
- matches a single character from the set/range you specify.

### **Examples**
ls file[1-3].txt	Matches file1.txt, file2.txt, file3.txt.
ls file[abc].txt	Matches filea.txt, fileb.txt, filec.txt
Matches any fileX.txt except where X is a digit


## **{}**
- Generates a sequence or comma-separated list of items.

### **Examples**
echo file{1,2,3}.txt	Expands to file1.txt file2.txt file3.txt.
mkdir project/{docs,src,bin}	Creates dirs project/docs, src, bin.
cp file{A..Z}.txt /tmp/	Copy all files from fileA.txt to fileZ.txt.
This is not technically a wildcard but a bash feature


## **~**
- Expands to the home directory of the current user

### **Examples**
cd ~	Go to your home directory.
cp ~/Documents/* .	Copy all files from Documents to current dir.



## ** . and .. **
- . = current directory
- .. = parent directory

### **Examples**
ls .	List current directory contents.
cd ..	Move up one level in directory tree.



## **!**
- Negates a character set in []

### **Examples**
ls file[!a-c].txt	Matches files not ending with a, b, c.


## **\**
- escapes the special meaning of a wildcard.

### **Examples**
ls \*	Lists file named *, not all files.
echo file\?.txt	Treats ? literally, not as a wildcard.


Bonus

Wildcards don’t have options directly but are affected by shell behavior and command options:
	•	shopt -s dotglob
👉 Make * match hidden files (dotfiles).
	•	find . -name "*.txt"
👉 Use find with wildcards for recursive matching.
	•	ls -d */
👉 Match only directories.


## **$**
- Used to reference or expand a variable or expression. It tells the shell:
“Hey, don’t treat this as a literal word — go get me the value of it.”

Common Uses of $

🔹 1. Accessing Variables

USER="shadowman76"
echo $USER

	$USER retrieves the value stored in the USER variable.
	•	No $ means you’re referencing the variable name literally, not the value.


