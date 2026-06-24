#!/bin/bash
ANSWER=""
if command -v zenity &> /dev/null; then
    zenity --question --text="Do you want to continue with Waydroid?" 2>/dev/null && ANSWER="yes"
elif command -v kdialog &> /dev/null; then
    kdialog --yesno "Do you want to continue with Waydroid?" 2>/dev/null && ANSWER="yes"
else
    echo "zenity or kdialog not found, please install one of them by your package manager"
    exit 1
fi
if [ "$ANSWER" == "yes" ]; then
    waydroid show-full-ui
else
    exit 1
fi
