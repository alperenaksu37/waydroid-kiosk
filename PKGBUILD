# Maintainer: Alperen Aksu <alperenaksu6024@gmail.com>
pkgname=waydroid-kiosk
pkgver=1.0
pkgrel=1
pkgdesc="Waydroid kiosk mode for Cage with prompt as login session"
arch=('any')
url="https://github.com/alperenaksu37/waydroid-kiosk"
license=('Unlicense')
depends=('cage' 'waydroid' 'zenity')

package() {
    install -Dm755 "${srcdir}/usr/local/bin/waydroid-kiosk.sh" "${pkgdir}/usr/local/bin/waydroid-kiosk.sh"
    install -Dm644 "${srcdir}/usr/share/wayland-sessions/waydroid-kiosk.desktop" "${pkgdir}/usr/share/wayland-sessions/waydroid-kiosk.desktop"
    install -Dm644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
