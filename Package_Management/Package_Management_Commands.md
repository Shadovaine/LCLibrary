# **Package Management**

## **Commands used in installing, upgrading, and purging packages.**

## **Table of Contents
- `apt`
- `snap`
- `dkpg`
- `yum`
- `dnf`
- `rpm`
- `flatpak`
  
## **Command: apt (Advanced Package Tool)**
**Description** Used on Debian-based Linux systems (Ubuntu, Linux Mint, Kali).

## **Syntax**
- apt [OPTIONS] COMMAND [PACKAGE...]

### **Options**
- `apt update`:  Refreshees the package index from repositories.
- `apt upgrade`:  Upgrades all upgradable packages.
- `apt full-upgrade`:  Upgrades packages and handles changing dependenices.
- `apt install <pkg>`:  Installs a package.
- `apt remove <pkg>`:  Removes a package.
- `apt purge <pkg>`:  Removes a package and its configuration files.
- `apt autoremove`:  Removes automatically installed packages no longer needed.
- `apt search <term>`:  Searches for a pacakge by name or description.
- `apt show <pkg>`:  Displays detailed package information.
- `apt list`:  lists packages based on filters.
- `apt download <pkg>`:  Downloads a package .deb file without installing it.
- `apt edit-sources`:  Opens the sources list for editing.
- `-y`:  assume "yes" to all prompts.
- `-q`:  Quiet mode.
- `-qq`:  Super quiet mode.
- `-s` or `--simulate`:  Simulates the action with out making changes.
- `-d` or `--download-only`:  Download packages but does not install.
- `-o` <key>=<value>`:  Override configuration.
- `--purge`:  Removes packages including configuration files.
- `--reinstall`:  Reinstalls the specified packages.
- `--fix-broken`:  Fixes broken dependencies.
- `--no-install-recommends`:  Installs packages without recommended dependencies.
- `--fix-missing`:  Attempts to fix missing packages during installations. 
- `apt policy <pkg>`:  Show the candidate version and repo for a package.
- `apt-cache stats`:  Displays cache statistics.
  
### **Examples**

**Update repositories:**

```bash
sudo apt update
```
**Breakdown**
- `sudo`:  Makes user temporary superuser command.
- `apt`:  Package manager command.
- `update`: Refreshes the package index from repositories.

**Upgrade all packages:**

```bash
sudo apt upgrade
```
**Breakdown**
- `sudo`:  Temporary superuser command.
- `apt`:  Package manager command.
- `upgrade`:  Upgrades all upgradable packages.
  
**Install nmap:**

```bash
sudo apt install nmap
```
**Breakdown**
- `sudo`:  Temporary superuser command.
- `apt`:  Package Manager command.
- `install`:  Directs to install target package.
- `nmap`:  Target package to install.

**Remove package (keep configs):**

```bash
sudo apt remove apache2
```
**Breakdown**
- `sudo`:  Temporary superuser command.
- `apt`:  Package Manager command.
- `remove`:  Directs to remove target package.
- `apache2`:  Target package to remove.

**Purge package (remove configs also):**

```bash
sudo apt purge apache2
```
**Breakdown**
- `sudo`:  Temporary superuser command.
- `apt`:  Package Manager command.
- `purge`:  Directs to delete target package.
- `apache2`:  Target package to delete.
  

## **Command: snap**
**Description** Used for Snap packages (sandboxed apps, Ubuntu’s default).

## **Syntax**
- snap [OPTIONS] COMMAND [PACKAGE...]

### **Options**
- `snap install <pkg>`:  Installs a snap package.
- `snap remove <pkg>`:  Removes a snap package.
- `snap refresh <pkg>`:  Updates a snap package.
- `snap revert <pkg>`:  Rolls back to the previous version.
- `snap list`:  Lists installed snap packages.
- `snap find <term>`:  Searches the Snap Store for packages.
- `snap info <pkg>`:  Shows details about a snap package.
- `snap run <pkg>`:  Runs a snap package.
- `--channel=<track>/<risk>`:  Install from a specific channel.
- `--revision=<numbers>`:  Install a specific revision.
- `--classic`:  Install with a classic confinement.
- `snap enable <pkg>`:  Enables a previously disabled snap.
- `snap disable <pkg>`:  Disables a snap without uninstalling it.
- `snap connections`:  shows all snap interface connections.
- `snap connect`:  Manually connect a snap interface.
- `snap disconnect`:  Disconnect a snap interface.
- `snap interface <int>`:  Show details of a specific interface.
- `snap aliases`:  Shows current snap command aliases.
- `snap alias`:  Creates a command alias for a snap.
- `snap unalias`:  Removes a command alias.
- `snap warnings`:  show warnings for snaps.
- `snap changes`:  Lists recent snap changes and transactions.
- `snap change <id>`:  Show details for a specific change ID.
- `snap abort <id>`:  Aborts a pending snap change.
- `snap services`:  Lists snap services and their status.
- `snap start <svc>`:  Starts a snap service.
- `snap stop <svc>`:  Stops a snap services.
- `snap restart <svc>`:  Restarts a snap service.
- `snap set <pkg> key=value`:  Set configuration for a snap.
- `snap get <pkg>`:  Get configurations for a snap.

### **Examples**

**Search for VS Code:**

```bash
snap find code
```
**Breakdown**
- `snap`:  Package manager command.
- `find`: Directs package manager to find target package.
- `code`:  Target package to search for.
  
**Install VS Code:**

```bash
sudo snap install code --classic
```

**Update snaps:**

```bash
sudo snap refresh
```


## **dpkg (Debian Package Manager)**
**Description** The low-level package manager for handling .deb files.

## **Syntax**
- dpkg [OPTIONS] PACKAGE

### **Options**
i FILE.deb	Install a .deb file.
-r PACKAGE	Remove a package.
-P PACKAGE	Purge (remove configs too).
-l	List installed packages.
-L PACKAGE	List files installed by a package.

### **Example**

**Install a .deb file:**

```bash
sudo dpkg -i google-chrome.deb
```
**Remove a package:**

```bash
sudo dpkg -r google-chrome-stable
```
 
**List installed packages:**

```bash
dpkg -l
```

**List package contents:**

```bash
dpkg -L vim
```


## **Command: yum (Yellowdog Updater Modified)**
**Description** For RHEL/CentOS 7 and earlier. (Now mostly replaced by dnf).

## **Syntax**
- yum [OPTIONS] COMMAND [PACKAGE...]

### **Options**
install PACKAGE	Install a package.
remove PACKAGE	Remove a package.
update	Update all packages.
search TERM	Search for a package.

### **Examples**

**Install httpd:**

```bash
sudo yum install httpd
```

**Update all packages:**

```bash
sudo yum update
```

**Search for nginx:**

```bash
yum search nginx
```


## **Command: dnf (Dandified YUM)**
**Description** The modern replacement for yum on RHEL/CentOS 8+ and Fedora.

## ** Syntax**
- dnf [OPTIONS] COMMAND [PACKAGE...]

### **Options**
install PACKAGE	Install a package.
remove PACKAGE	Remove a package.
upgrade	Upgrade all packages.
search TERM	Search for a package.

### **Examples**

Install git:

```bash
sudo dnf install git
```

**Upgrade all packages:**

```bash
sudo dnf upgrade
```

**Search for docker:**

```bash
dnf search docker
```


## **Command: rpm (Red Hat Package Manager)**
**Description** Low-level package manager for .rpm files.

## **Syntax**
- rpm [OPTIONS] PACKAGE

### **Options**
-i FILE.rpm	Install a .rpm file.
-e PACKAGE	Remove a package.
-q PACKAGE	Query package status.
-ql PACKAGE	List installed files from package.

### **Examples**

**Install a .rpm file:**

```bash
sudo rpm -i package.rpm
```

**Query installed package:**

```bash
rpm -q httpd
```

**List files installed by package:**

```bash
rpm -ql httpd
```


## **Command: flatpak**
**Description** For Flatpak apps (cross-distro sandboxed apps).

## **Syntax**
- flatpak [OPTIONS] COMMAND [PACKAGE...]

### **Options**
search TERM	Search for apps.
install REMOTE APP	Install an app.
run APP	Run an installed app.
update	Update installed apps.

### **Examples**

**Search for Spotify:**

```bash
flatpak search spotify
```

**Install Spotify:**

```bash
sudo flatpak install flathub com.spotify.Client
```

**Run Spotify:**

```bash
flatpak run com.spotify.Client
```

