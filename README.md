# Waydroid Kiosk
Waydroid kiosk mode for Cage with prompt as login session

## Features
- **Waydroid in full screen:** You can run it like it's native because it uses Cage which is a Wayland compositor for full screen kiosk. For people who don't know, Waydroid is a tool for running Android in Wayland without emulation.
- **Confirmation dialog:** It shows a confirmation dialog before booting Waydroid. If you forget your setting on "Waydroid Kiosk" option, you can select "No" and it returns to login screen.

## How to escape from session
### On v2.0 and newer
If your Android version is Android 12 or newer, you can escape easily without powering off your computer!
1. Open quick settings on Android session
2. Select power button and "Power off" option on power menu
3. Wait for powering off Android
4. Select "Exit" on runner menu

### On 1.0
You can't escape without powering off your computer because Cage is written for kiosk devices.
1. Power off Android session by quick settings (optional if you want to prevent data loss)
2. Press power off button on your machine
3. After powering on, don't forget to select your desktop environment!

## How to build
You don't need to build it if you're using Debian-based or Arch-based distro, because I compiled it for them. But *if you want, you can*.

1. Copy the repository with git:
  ```bash
  git clone https://github.com/alperenaksu37/waydroid-kiosk
  ```
  If you're using Arch Linux, `git` may not be installed. If you have gotten `command not found` error, install it with `sudo pacman -S git`.

2. Go to directory:
  ```bash
  cd waydroid-kiosk/
  ```
  
### For Debian
3. Set the owner of directory (recursively) to root:
  ```bash
  sudo chown -R root:root src/
  ```
4. Compile it by `dpkg-deb` (no package installation required):
  ```bash
  dpkg-deb --build src/ waydroid-kiosk_2.0_all.deb
  ```
5. Install it:
  ```bash
  sudo apt-get install waydroid-kiosk_2.0_all.deb
  ```

### For Arch Linux
3. Check the `base-devel` package:
  ```bash
  sudo pacman -S --needed base-devel
  ```
4. Start building:
  ```bash
  makepkg -si
  ```
  This command **will automatically install** the package.
