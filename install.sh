#!/bin/bash
clear
echo "Установка MemoPad:"
echo "------------------"

export MEMOPAD_DIR="$HOME/.local/share/memopad"

mkdir -vp "$MEMOPAD_DIR"
mkdir -vp "$MEMOPAD_DIR/modules" && mkdir -vp "$MEMOPAD_DIR/help"

cp "./modules"/*.py -vu "$MEMOPAD_DIR/modules"
cp "./help"/*.py -vu "$MEMOPAD_DIR/help"
cp ./*.py -vu "$MEMOPAD_DIR" 

cd "$MEMOPAD_DIR" && echo "$PWD"

echo "ln 'main.py' -> 'memopad'"
if test -e "$MEMOPAD_DIR/memopad"; then
  rm "$MEMOPAD_DIR/memopad" && ln main.py memopad
else
  ln main.py memopad
fi

MEMOPAD_PATH="$HOME/.local/share/memopad"

if test -e "$HOME/.bash_profile"; then
  SHELL_FILE="$HOME/.bash_profile"
elif test -e "$HOME/.profile"; then
  SHELL_FILE="$HOME/.profile"
elif test -e "$HOME/.bashrc"; then
  SHELL_FILE="$HOME/.bashrc"
fi

{
  echo "" && echo "# Add MemoPad Path"
  echo 'export PATH="$PATH:'"$MEMOPAD_PATH\""
} >> "$SHELL_FILE"
echo  "PATH='$MEMOPAD_PATH'" "->" "'$SHELL_FILE'"


echo "--------------------"
echo "Установка завершена."
