
# 🐧 Linux Command Library

Welcome to my personal Linux command library — a curated collection of commands, options, and breakdowns as I train for the CompTIA Linux+ certification and real-world sysadmin work.

## 📁 Topics Covered

- Archiving & Compression
- Disk and FileSystem Management
- File & Directory Management
- Networking Tools
- Package Management
- Permissions & Ownership
- Process Management
- Scripting & Automation
- Search & Filter Management
- Security Hardening
- System Information and Monitoring
- TroubleShooting Management
- User & Group Management
- WildCards
- Viewing and Edit Management

### 📌 Example Command: `find` 
Search for Files Matching Criteria

<pre>
bash
find /etc -type f -name "*.conf" -user root -mtime -2

</pre>	

 **Breakdown**:
 - `find`: Search utility
 - `/etc`: Starting directory
 - `-type f`: Files only
 - `-name "*.conf"`: Only `.conf` files
 - `-user root`: Owned by root
 - `-mtime -2`: Modified in the last 2 days
	
