# Waydroid Kiosk
Waydroid kiosk mode for Cage with prompt as login session

## How to build
- Copy the repository with git:
  ```bash
  git clone https://github.com/alperenaksu37/waydroid-kiosk
  ```
  If you're using Arch Linux, `git` may not be installed. If you have gotten `command not found` error, install it with `sudo pacman -S git`.
- Go to directory:
  ```bash
  cd waydroid-kiosk/
  ```
  
### For Debian
- Set the owner of directory (recursively) to root:
  ```bash
  sudo chown -R root:root src/
  ```
- Compile it by `dpkg-deb` (no package installation required):
  ```bash
  dpkg-deb --build src/ waydroid-kiosk_1.0_all.deb
  ```
- Install it:
  ```bash
  sudo apt-get install waydroid-kiosk_1.0_all.deb
  ```

### For Arch Linux
- Check the `base-devel` package:
  ```bash
  sudo pacman -S --needed base-devel
  ```
- Start building:
  ```bash
  makepkg -si
  ```
  This command will automatically install the package.
