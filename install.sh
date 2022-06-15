#!/bin/bash

apt update && echo "S" | apt upgrade
echo "S" | apt install python3 python3-pip
echo "S" | apt-get install python3-wxgtk4.0
echo "S" | apt-get install build-essential python3-dev libwebkit2gtk-4.0-dev libtiff-dev libnotify-dev freeglut3-dev libsdl1.2-dev libgstreamer-plugins-base1.0-dev 
echo "S" | pip3 install wxPython threading youtube_dl 
mkdir "/opt/downtube_v2.0"
cp -r * "/opt/downtube_v2.0"
touch /usr/share/applications/ytube_v2.desktop
echo "[Desktop Entry]" >> /usr/share/applications/ytube_v2.desktop
echo "Type=Application" >> /usr/share/applications/ytube_v2.desktop
echo "Icon=/opt/downtube_v2.0/iconyou.png" >> /usr/share/applications/ytube_v2.desktop
echo "Name=DownTube v2.0" >> /usr/share/applications/ytube_v2.desktop
echo "Exec=python3 /opt/downtube_v2.0/run_v2.py" >> /usr/share/applications/ytube_v2.desktop
echo "NoDisplay=false" >> /usr/share/applications/ytube_v2.desktop
echo 
echo "Pronto ..."
