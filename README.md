
# 🐧 Linux Command Library

Welcome to my personal Linux command library — a curated collection of commands, options, and breakdowns as I train for the CompTIA Linux+ certification and real-world sysadmin work.

## 📁 Topics Covered

- File & Directory Management
- User & Group Commands
- Permissions & Ownership
- Networking Tools
- Process Management
- Archiving & Compression (`tar`, `gzip`, etc.)
- Scripting & Automation
- Security Hardening

### 📌 Example Command: `find` 
Search for Files Matching Criteria

```find /etc -type f -name "*.conf" -user root -mtime -2```
 

	- `-find`: Search command
	-  `/etc`: Start directory
	- `-type f`: Find files only
	- `-name "*.conf"`: Config files
	- `-user root`: Owned by root
	- `-mtime -2`: Modified in the last 2 days
