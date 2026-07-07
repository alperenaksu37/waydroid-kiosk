# Waydroid Kiosk
Waydroid kiosk mode for Cage with prompt as login session

## Features
- **Waydroid in full screen:** You can run it like it's native because it uses Cage which is a Wayland compositor for full screen kiosk. For people who don't know, Waydroid is a tool for running Android in Wayland without emulation.
- **Confirmation dialog:** It shows a confirmation dialog before booting Waydroid. If you forget your setting on "Waydroid Kiosk" option, you can select "No" and it returns to login screen.

## How to escape from session
I can't add an option for auto closing because Waydroid doesn't stop when you shut down the system by quick settings. And Cage doesn't allow escaping because it is written for kiosk mode. The only escaping way is shutting down computer with power button. I'm sorry for this issue.

And don't forget to select your old desktop environment!

## How to build
You don't need to build it if you're using Debian-based or Arch-based distro, because I compiled it for them. But *if you want, you can*.

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
  This command **will automatically install** the package.
