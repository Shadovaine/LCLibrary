# Package Management

## Commands used in installing, upgrading, and purging packages

## Table of Contents

- `apt`
- `snap`
- `dkpg`
- `yum`
- `dnf`
- `rpm`
- `flatpak`
  
# Command: apt (Advanced Package Tool)

## Description: Used on Debian-based Linux systems (Ubuntu, Linux Mint, Kali)

## Syntax

- `apt [OPTIONS] COMMAND [PACKAGE...]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `apt update` | Refreshees the package index from repositories. | `apt update` |
| `apt upgrade`| Upgrades all upgradable packages. | `apt upgrade` |
| `apt full-upgrade` | Upgrades packages and handles changing dependenices. | `apt full-upgrade` |
| `apt install <pkg>`| Installs a package. | `apt install package-name` |
| `apt remove <pkg>` | Removes a package. | `apt remove package-name` |
| `apt purge <pkg>` | Removes a package and its configuration files. | `apt purge package-name` |
| `apt autoremove` | Removes automatically installed packages no longer needed. | `apt autoremove` |
| `apt search <term>` | Searches for a pacakge by name or description. | `apt search "term"` |
| `apt show <pkg>` | Displays detailed package information. | `apt show package-name` |
| `apt list` | lists packages based on filters. | `apt list` |
| `apt download <pkg>` |  Downloads a package .deb file without installing it. | `apt download package-name` |
| `apt edit-sources` | Opens the sources list for editing. | `apt edit-sources` |
| `-y` | Assume "yes" to all prompts. | `apt -y` |
| `-q` | Quiet mode. | `apt -q` |
| `-qq`| Super quiet mode. | `apt -qq` |
| `-s` or `--simulate` | Simulates the action with out making changes. | `apt -s` |
| `-d` or `--download-only` |  Download packages but does not install. | `apt -d package-name` |
| `--reinstall` | Reinstalls the specified packages. | `apt --reinstall package-name` |
| `--fix-broken` | Fixes broken dependencies. | `apt --fix-broken package-name`|
  
### Examples

### Update repositories

```bash
sudo apt update
```

### Breakdown

- `sudo`:  Makes user temporary superuser command.
- `apt`:  Package manager command.
- `update`: Refreshes the package index from repositories.

### Upgrade all packages

```bash
sudo apt upgrade
```

### Breakdown

- `sudo`:  Temporary superuser command.
- `apt`:  Package manager command.
- `upgrade`:  Upgrades all upgradable packages.
  
### Install nmap

```bash
sudo apt install nmap
```

### Breakdown

- `sudo`:  Temporary superuser command.
- `apt`:  Package Manager command.
- `install`:  Directs to install target package.
- `nmap`:  Target package to install.

### Remove package (keep configs)

```bash
sudo apt remove apache2
```

### Breakdown

- `sudo`:  Temporary superuser command.
- `apt`:  Package Manager command.
- `remove`:  Directs to remove target package.
- `apache2`:  Target package to remove.

### Purge package (remove configs also)

```bash
sudo apt purge apache2
```

### Breakdown

- `sudo`:  Temporary superuser command.
- `apt`:  Package Manager command.
- `purge`:  Directs to delete target package.
- `apache2`:  Target package to delete.
  
# Command: snap

## Description: Used for Snap packages (sandboxed apps, Ubuntu’s default)

## Syntax

- `snap [OPTIONS] COMMAND [PACKAGE...]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `snap install <pkg>` | Installs a snap package. | `snap install package-name` |
| `snap remove <pkg>` | Removes a snap package. | snap remove package-name` |
| `snap refresh <pkg>` | Updates a snap package. | `snap refresh` |
| `snap revert <pkg>`| Rolls back to the previous version. | `snap revert package-name` |
| `snap list` | Lists installed snap packages. | `snap list` |
| `snap find <term>` | Searches the Snap Store for packages. `snap find name` |
| `snap info <pkg>` | Shows details about a snap package. | `snap info name` |
| `snap run <pkg>` | Runs a snap package. | `snap run name` |
| `--channel=<track>/<risk>` | Install from a specific channel. | `snap --channel=10` |
| `--revision=<numbers>` | Install a specific revision. | `snap --revision=3` |
| `--classic` | Install with a classic confinement. | `snap --classic` |
| `snap enable <pkg>` | Enables a previously disabled snap. | `snap enable package-name` |
| `snap disable <pkg>` | Disables a snap without uninstalling it. | `snap diable package-name` |
| `snap connections` | Shows all snap interface connections. | snap connections` |
| `snap connect` | Manually connect a snap interface. | snap connect name` |
| `snap disconnect` | Disconnect a snap interface. | snap disconnect name` |
| `snap interface <int>` | Show details of a specific interface. | `snap interface name` |
| `snap aliases` | Shows current snap command aliases. | `snap aliases` |
| `snap alias` | Creates a command alias for a snap. | `snap alias` |
| `snap unalias` | Removes a command alias. | snap unalias` |
| `snap warnings` | Show warnings for snaps. | `snap warnings` |
| `snap changes` | Lists recent snap changes and transactions. | `snap changes` |
| `snap change <id>` | Show details for a specific change ID. | `snap change 3333` |
| `snap abort <id>` | Aborts a pending snap change. | `snap abort 2222` |
| `snap services` | Lists snap services and their status. | `snap services` |
| `snap start <svc>` | Starts a snap service. | `snap start name.service` |
| `snap stop <svc>` | Stops a snap services. | `snap stop name.service` |
| `snap restart <svc>` | Restarts a snap service. | `snap restart name.service` |
| `snap set <pkg> key=value` | Set configuration for a snap. | `snap set package-name` |
| `snap get <pkg>` | Get configurations for a snap. | `snap get package-name` |

### Examples

### Search for VS Code

```bash
snap find code
```

### Breakdown

- `snap`:  Package manager command.
- `find`: Directs package manager to find target package.
- `code`:  Target package to search for.
  
### Install VS Code

```bash
sudo snap install code --classic
```

### Update snaps

```bash
sudo snap refresh
```

# Command: dpkg (Debian Package Manager)

## Description: The low-level package manager for handling .deb files

## Syntax

- `dpkg [OPTIONS] PACKAGE`

### Options

i FILE.deb	Install a .deb file.
-r PACKAGE	Remove a package.
-P PACKAGE	Purge (remove configs too).
-l	List installed packages.
-L PACKAGE	List files installed by a package.

### Examples

### Install a .deb file

```bash
sudo dpkg -i google-chrome.deb
```

### Remove a package

```bash
sudo dpkg -r google-chrome-stable
```
 
### List installed packages

```bash
dpkg -l
```

### List package contents

```bash
dpkg -L vim
```

# Command: yum (Yellowdog Updater Modified)

## Description: For RHEL/CentOS 7 and earlier. (Now mostly replaced by dnf)

## Syntax

- `yum [OPTIONS] COMMAND [PACKAGE...]`

### Options

install PACKAGE	Install a package.
remove PACKAGE	Remove a package.
update	Update all packages.
search TERM	Search for a package.

### Examples

### Install httpd

```bash
sudo yum install httpd
```

### Update all packages

```bash
sudo yum update
```

### Search for nginx

```bash
yum search nginx
```

# Command: dnf (Dandified YUM)

## Description: The modern replacement for yum on RHEL/CentOS 8+ and Fedora.

## Syntax

- `dnf [OPTIONS] COMMAND [PACKAGE...]`

### Options

install PACKAGE	Install a package.
remove PACKAGE	Remove a package.
upgrade	Upgrade all packages.
search TERM	Search for a package.

### Examples

### Install git

```bash
sudo dnf install git
```

### Upgrade all packages

```bash
sudo dnf upgrade
```

### Search for docker

```bash
dnf search docker
```

# Command: rpm (Red Hat Package Manager)

## Description: Low-level package manager for .rpm files

## Syntax

- `rpm [OPTIONS] PACKAGE`

### Options

-i FILE.rpm	Install a .rpm file.
-e PACKAGE	Remove a package.
-q PACKAGE	Query package status.
-ql PACKAGE	List installed files from package.

### Examples

### Install a .rpm file

```bash
sudo rpm -i package.rpm
```

### Query installed package

```bash
rpm -q httpd
```

### List files installed by package

```bash
rpm -ql httpd
```

# Command: flatpak

## Description: For Flatpak apps (cross-distro sandboxed apps)

## Syntax

- `flatpak [OPTIONS] COMMAND [PACKAGE...]`

### Options

search TERM	Search for apps.
install REMOTE APP	Install an app.
run APP	Run an installed app.
update	Update installed apps.

### Examples

### Search for Spotify

```bash
flatpak search spotify
```

### Install Spotify

```bash
sudo flatpak install flathub com.spotify.Client
```

### Run Spotify

```bash
flatpak run com.spotify.Client
```
