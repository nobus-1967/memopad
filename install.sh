#!/bin/bash
clear
echo "Установка MemoPad:"
echo "------------------"

echo "mkdir $MEMOPAD"

export MEMOPAD="$HOME/.local/bin/memopad"
mkdir -vp "$MEMOPAD"
mkdir -vp "$MEMOPAD/modules"
mkdir -vp "$MEMOPAD/help"

echo "cp *.py -> $MEMOPAD"

cp "./modules"/*.py -vu "$MEMOPAD/modules"
cp "./help"/*.py -vu "$MEMOPAD/help"
cp ./*.py -vu "$MEMOPAD"

echo "cd $HOME => $MEMOPAD"

cd "$MEMOPAD" && echo "$PWD"

echo "ln 'main.py' -> 'memopad'"

if test -e "$MEMOPAD/memopad"; then
rm "$MEMOPAD/memopad" && ln main.py memopad
else
ln main.py memopad
fi

echo "--------------------"
echo "Установка завершена."

