# Waydroid Kiosk
Waydroid kiosk mode for Cage with prompt as login session

## How to build
Copy the repository with git:
```bash
git clone https://github.com/alperenaksu37/waydroid-kiosk
```
If you're using Arch Linux, `git` may not be installed. If you have gotten `command not found` error, install it with `sudo pacman -S git`.

### For Debian
- Remove `.git` directory:
  ```bash
  rm -r waydroid-kiosk/.git/
  ```
- Set the owner of directory (recursively) to root:
  ```bash
  sudo chown -R root:root waydroid-kiosk/
  ```
- Compile it by `dpkg-deb` (no package installation required):
  ```bash
  dpkg-deb --build waydroid-kiosk/ waydroid-kiosk_1.0_all.deb
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
- Go to directory:
  ```bash
  cd waydroid-kiosk/
  ```
- Start building and installing:
  ```bash
  makepkg -si
  ```
