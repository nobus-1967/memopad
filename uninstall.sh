#!/bin/bash
clear
echo "Удаление MemoPad:"
echo "------------------"

export MEMOPAD="$HOME/.local/share/memopad"
rm -rv "$MEMOPAD"

echo "--------------------"
echo "Удаление завершено."
