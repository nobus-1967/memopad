#!/bin/bash
clear
echo "Установка MemoPad:"
echo "------------------"

export MEMOPAD="$HOME/.local/share/memopad"
mkdir -vp "$MEMOPAD"
mkdir -vp "$MEMOPAD/modules"
mkdir -vp "$MEMOPAD/help"

cp "./modules"/*.py -vu "$MEMOPAD/modules"
cp "./help"/*.py -vu "$MEMOPAD/help"
cp ./*.py -vu "$MEMOPAD"

cd "$MEMOPAD" && echo "$PWD"

echo "ln 'main.py' -> 'memopad'"
if test -e "$MEMOPAD/memopad"; then
rm "$MEMOPAD/memopad" && ln main.py memopad
else
ln main.py memopad
fi

echo "PATH -> ~/.bashrc"
echo '' >> "$HOME/.bashrc"
echo '# Add MemoPad Path' >> "$HOME/.bashrc"
echo 'export PATH="$PATH:$HOME/.local/share/memopad"' >> "$HOME/.bashrc"

echo "--------------------"
echo "Установка завершена."

