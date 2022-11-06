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

if test -e "$HOME/.bash_profile"; then
    echo '' >> "$HOME/.bash_profile"
    echo '# Add MemoPad Path' >> "$HOME/.bash_profile"
    echo 'export PATH="$PATH:$HOME/.local/share/memopad"' >> "$HOME/.bash_profile"
    echo 'PATH="$PATH:$HOME/.local/share/memopad" -> "$HOME/.bash_profile"' 
elif test -e "$HOME/.profile"; then
    echo '' >> "$HOME/.profile"
    echo '# Add MemoPad Path' >> "$HOME/.profile"
    echo 'export PATH="$PATH:$HOME/.local/share/memopad"' >> "$HOME/.profile"
    echo 'PATH="$PATH:$HOME/.local/share/memopad" -> "$HOME/.profile"'
elif test -e "$HOME/.bashrc"; then    
    echo '' >> "$HOME/.bashrc"
    echo '# Add MemoPad Path' >> "$HOME/.bashrc"
    echo 'export PATH="$PATH:$HOME/.local/share/memopad"' >> "$HOME/.bashrc"
    echo 'PATH="$PATH:$HOME/.local/share/memopad" -> "$HOME/.bashrc"'
fi

echo "--------------------"
echo "Установка завершена."

