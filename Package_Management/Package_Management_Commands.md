# **Package Management**

## **apt (Advanced Package Tool)**
- Used on Debian-based systems (Ubuntu, Linux Mint, Kali).

## **Syntax**
- apt [OPTIONS] COMMAND [PACKAGE...]

### **Options**
update	Update package index (fetches latest lists).
upgrade	Upgrade installed packages.
install PACKAGE	Install a package.
remove PACKAGE	Remove a package (keeps configs).
purge PACKAGE	Remove package and configs.
search TERM	Search for a package.
show PACKAGE	Show package details.

#### **Examples**
Update repositories:
sudo apt update

Upgrade all packages:
sudo apt upgrade

Install nmap:
sudo apt install nmap

Remove package (keep configs):
sudo apt remove apache2

Purge package (remove configs too):
sudo apt purge apache2


## **snap**
-Used for Snap packages (sandboxed apps, Ubuntu’s default).

## **Syntax**
- snap [OPTIONS] COMMAND [PACKAGE...]

### **Options**
find TERM	Search for a snap package.
install PACKAGE	Install a snap package.
remove PACKAGE	Remove a snap package.
refresh	Update installed snaps.

#### **Examples**
Search for VS Code:
snap find code

Install VS Code:
sudo snap install code --classic

Update snaps:
sudo snap refresh


## **dpkg (Debian Package Manager)**
- The low-level tool for handling .deb files.

## **Syntax**
- dpkg [OPTIONS] PACKAGE

### **Options**
i FILE.deb	Install a .deb file.
-r PACKAGE	Remove a package.
-P PACKAGE	Purge (remove configs too).
-l	List installed packages.
-L PACKAGE	List files installed by a package.

#### **Example**
Install a .deb file:
sudo dpkg -i google-chrome.deb

Remove a package:
sudo dpkg -r google-chrome-stable

 List installed packages:
dpkg -l

List package contents:
dpkg -L vim



## **yum (Yellowdog Updater Modified)**
-For RHEL/CentOS 7 and earlier. (Now mostly replaced by dnf).

## **Syntax**
yum [OPTIONS] COMMAND [PACKAGE...]

### **Options**
install PACKAGE	Install a package.
remove PACKAGE	Remove a package.
update	Update all packages.
search TERM	Search for a package.

#### **Examples**
Install httpd:
sudo yum install httpd

Update all packages:
sudo yum update

Search for nginx:
yum search nginx


## **dnf (Dandified YUM)**
- The modern replacement for yum on RHEL/CentOS 8+ and Fedora.

## ** Syntax**
-dnf [OPTIONS] COMMAND [PACKAGE...]

### **Options**
install PACKAGE	Install a package.
remove PACKAGE	Remove a package.
upgrade	Upgrade all packages.
search TERM	Search for a package.

#### **Examples**
Install git:
sudo dnf install git

Upgrade all packages:
sudo dnf upgrade

Search for docker: 
dnf search docker


## **rpm (Red Hat Package Manager)**
-Low-level package management for .rpm files.

## **Syntax**
-rpm [OPTIONS] PACKAGE

### **Options**
-i FILE.rpm	Install a .rpm file.
-e PACKAGE	Remove a package.
-q PACKAGE	Query package status.
-ql PACKAGE	List installed files from package.

#### **Examples**
Install a .rpm file:
sudo rpm -i package.rpm

Query installed package:
rpm -q httpd

 List files installed by package:
rpm -ql httpd


## **flatpak**
- For Flatpak apps (cross-distro sandboxed apps).

## **Syntax**
- flatpak [OPTIONS] COMMAND [PACKAGE...]

### **Options**
search TERM	Search for apps.
install REMOTE APP	Install an app.
run APP	Run an installed app.
update	Update installed apps.

#### **Examples**
Search for Spotify:
flatpak search spotify

Install Spotify:
sudo flatpak install flathub com.spotify.Client

Run Spotify:
flatpak run com.spotify.Client


