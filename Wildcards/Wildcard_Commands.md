# Linux wildcards

## Description: Special characters used to represent unknown or variable parts

## Table of Contents

- `*`
- `?`
- `[]`
- `{}`
- `~`
- `.`
- `..`
- `!`
- `\`
- `$`

# Wildcard: *

## Description: Matches zero or more characters in a file name

### Examples

### List all files in the current directory

```bash
ls *.txt
```

### Delete all files ending with .txt

```bash
rm *.txt	
```

# Wildcard: ?

## Description: Matches exactly one character

### Examples

### Match file1.txt, fileA.txt

```bash
ls file?.txt
```

### Move all .jpg files with one character filenames into images

```bash
mv ?.jpg images/	
```

# Wildcard: []

## Description: Matches a single character from the set/range you specify

### Examples

### Matches file1.txt, file2.txt, file3.txt

```bash
ls file[1-3].txt
```

### Matches filea.txt, fileb.txt, filec.txt

```bash
ls file[abc].txt
```



# Wildcard: {}

## Description: Generates a sequence or comma-separated list of items

### Examples

### Expands to file1.txt file2.txt file3.txt

```bash
echo file{1,2,3}.txt
```

### Creates dirs project/docs, src, bin

```bash
mkdir project/{docs,src,bin}
```

cp file{A..Z}.txt /tmp/	Copy all files from fileA.txt to fileZ.txt.
This is not technically a wildcard but a bash feature


# Wildcard: ~

## Description: Expands to the home directory of the current user

### Examples

### Go to your home directory

```bash
cd ~	
```

### Copy all files from Documents to current directory

```bash
cp ~/Documents/* 
```




# Wildcard: .

## Description: One period stands for current directory

### Examples

List current directory contents

```bash
ls .
```

# Wildcard: ..

## Description: Two periods stand for parent directory


### Examples

### Move up one level in directory tree

```bash
cd ..	
```

# Wildcard: !

## Description: Negates a character set in []

### Examples

### Matches files not ending with a, b, c

```bash
ls file[!a-c].txt	
```

# Wildcard: \

## Description: Escapes the special meaning of a wildcard

### Examples

### Lists file named *, not all files

```bash
ls \*
```

# Bonus

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


