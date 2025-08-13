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

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Makes user temporary superuser command |
| `apt` | Package manager command |
| `update` | Refreshes the package index from repositories |

### Upgrade all packages

```bash
sudo apt upgrade
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary superuser command |
| `apt` | Package manager command |
| `upgrade` | Upgrades all upgradable packages |
  
### Install nmap

```bash
sudo apt install nmap
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary superuser command |
| `apt` | Package Manager command |
| `install` | Directs to install target package |
| `nmap` | Target package to install |

### Remove package (keep configs)

```bash
sudo apt remove apache2
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary superuser command |
| `apt` | Package Manager command |
| `remove` | Directs to remove target package |
| `apache2` | Target package to remove |

### Purge package (remove configs also)

```bash
sudo apt purge apache2
```

### Breakdown

| Breakdown | Decription |
|-----------|------------|
| `sudo` | Temporary superuser command |
| `apt` | Package Manager command |
| `purge` | Directs to delete target package |
| `apache2` | Target package to delete |
  
# Command: snap

## Description: Used for Snap packages (sandboxed apps, Ubuntu’s default)

## Syntax

- `snap [OPTIONS] COMMAND [PACKAGE...]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `snap install <pkg>` | Installs a snap package. | `snap install package-name` |
| `snap remove <pkg>` | Removes a snap package. | `snap remove package-name` |
| `snap refresh <pkg>` | Updates a snap package. | `snap refresh` |
| `snap revert <pkg>`| Rolls back to the previous version. | `snap revert package-name` |
| `snap list` | Lists installed snap packages. | `snap list` |
| `snap find <term>` | Searches the Snap Store for packages. | `snap find name` |
| `snap info <pkg>` | Shows details about a snap package. | `snap info name` |
| `snap run <pkg>` | Runs a snap package. | `snap run name` |
| `--channel=<track>/<risk>` | Install from a specific channel. | `snap --channel=10` |
| `--revision=<numbers>` | Install a specific revision. | `snap --revision=3` |
| `--classic` | Install with a classic confinement. | `snap --classic` |
| `snap enable <pkg>` | Enables a previously disabled snap. | `snap enable package-name` |
| `snap disable <pkg>` | Disables a snap without uninstalling it. | `snap diable package-name` |
| `snap connections` | Shows all snap interface connections. | `snap connections` |
| `snap connect` | Manually connect a snap interface. | `snap connect name` |
| `snap disconnect` | Disconnect a snap interface. | `snap disconnect name` |
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

| Breakdown | Description |
|-----------|-------------|
| `snap` | Package manager command |
| `find` | Directs package manager to find target package |
| `code` | Target package to search for |
  
### Install VS Code

```bash
sudo snap install code --classic
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary superuser command |
| `snap` | Package Manager Command |
| `install` | Directs to install specific package |
| `code --classic` | Specific package |

### Update snaps

```bash
sudo snap refresh
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary superuser command |
| `snap` | Package manager command |
| `refresh` | Directs to update all installed snap packages |

# Command: dpkg (Debian Package Manager)

## Description: The low-level package manager for handling .deb files

## Syntax

- `dpkg [OPTIONS] PACKAGE`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-i` | Install a .deb file | `sudo dpkg -i package.deb` |
| `-r` | Remove a package. | `sudo dpkg -r vim` |
| `-P` | Purge and remove configs too | `sudo dpkg -P vim` |
| `-l` | List installed packages | `dpkg-l | grep vim` |
| `-L` | List files installed by a package | `dpkg -L vim` |
| `-S` | Find which package owns a file | `dpkg -S /bin/ls` |
| `-s` | Show package status info | `dpkg -s vim` |
| `-I` | Show info about a .deb file | `dpkg -I packag.deb` |
| `-x` | Extract .deb contents to a folder | `dpkg -x package.deb /tmp/extracted` |
| `--configure <package>` | Reconfigure an unpacked package | `sudo dpkg --configure vim` |
| `--unpack <file.deb>` | Unpack without configuring | `sudo dpkg --unpack package.deb` |
| `--audit` | Show packages that are only partially installed | `dpkg --audit` |
| `--get-selections` | List selection states of packages | `dpkg --get-selections | grep vim` |
| `--set-selections` | Mark packages for install/remove | `echo "vim install" | sudo dpkg --set-selections` |
| `--update-avail` | Update available package info from /var/lib/dpkg/available | `sudo dpkg --update-avail` |
| `--clear-avail` | Clear available package info | `sudo dpkg --clear-avail` |

### Examples

### Install a .deb file

```bash
sudo dpkg -i google-chrome.deb
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary Superuser Commmand |
| `dpkg` | Package Manager Command |
| `-i` | Install a .deb package |
| `google-chrome.deb` | Specific pacakge to install |

### Remove a package

```bash
sudo dpkg -r google-chrome-stable
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary Superuser Command |
| `dpkg` | Package Manager Command |
| `-r` | Directs to remove a pacakge |
| `google.chrome-stable` | Specified pacakge to remove |

### List installed packages

```bash
dpkg -l
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `dpkg` | Package Manager Command |
| `-l` | Directs to list installed packages |

### List package contents

```bash
dpkg -L vim
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `dpkg` | Package Manager Command |
| `-L` | Directs to list package contents |
| `vim` | Specified package |

# Command: yum (Yellowdog Updater Modified)

## Description: For RHEL/CentOS 7 and earlier. (Now mostly replaced by dnf)

## Syntax

- `yum [OPTIONS] COMMAND [PACKAGE...]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `install` | Install a package | `sudo yum install vim` |
| `remove or erase` | Remove a package | `sudo yum remove vim` |
| `update` | Update all packages | `sudo yum update` |
| `upgrade` | UPdate packages and handle obsolete ones | `sudo yum upgrade` |
| `check-update` | Check for available updates without installing | `yum check-update` |
| `list` | List installed, available, or updates | `yum list installed` `yum list available` `yum list updates` |
| `info` | Show detailed info about a package | `yum info vim` |
| `search` | Search for a package | `yum search editor` |
| `provides/whatprovides` | Find which package provides a file or capability | `yum provides /bin/vim` |
| `clean` | Clear cached package data | `sudo yum clean all` |
| `makecache` | Download fresh repository metadata | `sudo yum makecache` |
| `history` | Show or manage transction history | `yum history` |
| `reinstall` | Reinstall a package | `sudo yum reinstall vim` |
| `downgrade` | Revert to an older package version | `sudo yum downgrade vim` |
| `group list` | list package groups | `yum group list` |
| `group install` | Install all package in a group | `sudo yum group install "Example list"` |
| `group remove` | Remove all packages in a group | `sudo yum group remove "Example List"` |
| `update-to` | Update a pacakge to a specific version | `sudo yum update-to vim 1.1.1` |

### Examples

### Install httpd

```bash
sudo yum install httpd
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary Superuser Command |
| `yum` | Package Manager Command |
| `install` | Directs to install specified package |
| `httpd` | Specified package |

### Update all packages

```bash
sudo yum update
```

### Breakdown 

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary Superuser command |
| `yum` | Package Manager Command |
| `update` | Specified command to update all packages |

### Search for nginx

```bash
yum search nginx
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `yum` | Package Manager Command |
| `search` | Directs to search for specified package |
| `nginx` | Specified package |

# Command: dnf (Dandified YUM)

## Description: The modern replacement for yum on RHEL/CentOS 8+ and Fedora.

## Syntax

- `dnf [OPTIONS] COMMAND [PACKAGE...]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `install` | Install a package | `sudo dnf install vim` |
| `remove` | Remove a package | `sudo dnf remove vim` |
| `upgrade` | Upgrade all packages | `sudo dnf upgrade` |
| `update` | Update all packages or a specific package | `sudo dnf update` |
| `check-update` | Check for available updates without installing | `dnf check-update` |
| `list` | List installed, available, or updates | `dnf list installed` `dnf list available` `dnf list updates` |
| `info` | Show detailed info about a package | `dnf info vim` |
| `search` | Search for a package by keyword | `dnf search editor` |
| `provides/whatprovides` | Find which package provides a file or capability | `dnf provides /bin/vim` |
| `clean` | Clear cached package data | `sudo dnf clean all` |
| `makecache` | Download fresh repository metadata | `sudo dnf makecache` |
| `history` | Show or manage transction history | `dnf history` |
| `reinstall` | Reinstall a package | `sudo dnf reinstall vim` |
| `downgrade` | Revert to an older package version | `sudo dnf downgrade vim` |
| `group list` | list package groups | `dnf group list` |
| `group install` | Install all package in a group | `sudo dnf group install "Example list"` |
| `group remove` | Remove all packages in a group | `sudo dnf group remove "Example List"` |
| `update-to` | Update a pacakge to a specific version | `sudo dnf update-to vim 1.1.1 ` |
| `repoquery` | Query information from enabled repos |  `dnf repoquery --available` |
| `autoremove` | Remove packages installed as dependencies but no longer needed | `sudo dnf autoremove` |

### Examples

### Install git

```bash
sudo dnf install git
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary Superuser command |
| `dnf` | Package Manager command |
| `install` | Directs to install specified package |
| `git` | Specified package |

### Upgrade all packages

```bash
sudo dnf upgrade
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo ` | Temporary Superuser Command |
| `dnf` | Package Manager Command |
| `upgrade` | Directs to upgrade all packages that can be ugraded |

### Search for docker

```bash
dnf search docker
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `dnf` | package Manager Command |
| `search` | Directs to search for a specified package |
| `docker` | Specified package |

# Command: rpm (Red Hat Package Manager)

## Description: Low-level package manager for .rpm files

## Syntax

- `rpm [OPTIONS] PACKAGE`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-i` | Install a .rpm file | `sudo rpm -i package.rpm` |
| `-e` | Remove a package | `sudo rpm -e vim` |
| `-q` | Query package status | `rpm -q` | 
| `-U` | Upgrade a package | `sudo rpm -U package.rpm` |
| `-F` | Freshen a package | `sudo rpm -F package.rpm` |
| `-qa` | Query all installed packages | `rpm -qa` |
| `-ql` | List installed files from package | `rpm -ql vim` |
| `-qf` | Find which package owns a file | `rpm -qf /bin/ls` |
| `-qi` | Show detailed package info | `rpm -qi vim` |
| `-qip` | Show info from a .rpm file | `rpm -qip package.rpm` |
| `-qp` | Query a package file | `rpm -qp package.rpm` |
| `-qpl` | List files inside a .rpm file | `rpm -qpl package. rpm` |
| `-v` | Verify installed package | `rpm -v vim` |
| `-Vp` | Verify a .rpm file | `rpm -Vp package.rpm` |
| `-test` | Test install/remove without making changes | `rpm -i -test package-rpm` |
| `--nodeps` | Ignore dependencies | `sudp rpm -i --nodeps package.rpm` |
| `--force` | Force install/upgrade | `sudo rpm -i --force package.rpm` |

### Examples

### Install a .rpm file

```bash
sudo rpm -i package.rpm
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary superuser command |
| `rpm` | Package manager command | 
| `-i` | Directs to install a specified pacakge |
| `package.rpm` | Specified package |

### Query installed package

```bash
rpm -q httpd
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `rpm` | Package manager command |
| `-q` | Query installed package |
| `httpd` | Specified package |

### List files installed by package

```bash
rpm -ql httpd
```

### Breakdown

| Breakdown | Description | 
|-----------|-------------|
| `rpm` | Package manager command |
| `-ql` | List installed files from package |
| `httpd` | Specified package to list |

# Command: flatpak

## Description: For Flatpak apps (cross-distro sandboxed apps)

## Syntax

- `flatpak [OPTIONS] COMMAND [PACKAGE...]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `search` | Search for apps | `flatpak search vscode` |
| `install REMOTE APP` | Install an app | `sudo flatpak install flathub org.example.com` |
| `uninstall [APP_ID]` | Remove an installed app | `sudo flatpak uninstall org.example.com` |
| `run APP` | Run an installed app |`flatpak run org.example.com` |
| `update` | Update installed apps | `sudo flatpak update` |
| `history` | Show history of installs/updates/removals |`flatpak history` |
| `config` | Show or change Flatpak configuration |`flatpak config` |
| `repair` | Check and fix Flatpak installation |`sudo flatpak repair`| 
| `permission-reset [APP_ID]` | Reset an app's permissions | `flatpak permission-reset org.example.com` |
| `permission-list` | List Flatpak app permissions |`flatpak permission-list` |
| `list` | List installed flatpak apps and runtimes |`flatpak list` |
| `info [APP_ID]` | Show detailed info about an app |`flatpak info org.example.com` |
| `override [APP_ID] [Options]` | Change app permissions |`sudo flatpak override org.example.com --filesystem=home` |
| `remote-delete [NAME]` | Remove a remote |`sudo flatpak remote-delete flathub` |
| `remote-add [NAME][URL]` | Add a new remote |`sudo flatpak remote-add flathub https://flathub.org/repo/flathub.flatpakrepo` |
| `remote-list` | List configured Flatpak remotes |`flatpak remote-list` |

### Examples

### Search for Spotify

```bash
flatpak search spotify
```
### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `flatpak` | Package manager command |
| `search` | Directs to search for a specified app |
| `spotify` | specified app to search for |

### Install Spotify

```bash
sudo flatpak install flathub com.spotify.Client
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary superuser command |
| `flatpak` | Package manager command |
| `install` | Directs manager to look at remote site for specified app |
| `flathub` | Remote repository of apps |
| `com.spotify.client` | specified app |

### Run Spotify

```bash
flatpak run com.spotify.Client
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `flatpak` | package manager command |
| `run` | Directs package manager to run specified app |
| `com.spotify.client` | Specified app to run |