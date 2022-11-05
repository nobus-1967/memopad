#!/bin/bash
clear
echo "Удаление MemoPad:"
echo "------------------"

echo "mkdir $MEMOPAD"

export MEMOPAD="$HOME/.local/bin/memopad"
rm -rv "$MEMOPAD"

echo "--------------------"
echo "Удаление завершено."


