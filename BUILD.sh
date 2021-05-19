# !/bin/bash
set -e

echo "**** BUILDING WITH FONTMAKE"
fontmake -u sources/Mekorot-Rashi-Regular.ufo -o ttf

echo "**** MOVING FONT FILES"
mkdir -p fonts/ttf
cp master_ttf/Mekorot-Rashi-Regular.ttf fonts/ttf/Mekorot-Rashi-Regular.ttf

echo "**** BUILDING SPECIMENS"
python3 documentation/drawbot/specimen-image-001.py
open documentation/drawbot/specimen-001.png

echo "**** REMOVING BUILD DIRECTORIES"
rm -rf master_ttf
