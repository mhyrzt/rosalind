#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 FOLDER_NAME"
    exit 1
fi

FOLDER_NAME=$1
MAIN_PY="$FOLDER_NAME/main.py"
OUT_TXT="$FOLDER_NAME/out.txt"
TXT_FILE=$(find "$FOLDER_NAME" -maxdepth 1 -type f -name "rosalind_*.txt" | head -n 1)

if [ ! -d "$FOLDER_NAME" ]; then
    echo "Error: Folder '$FOLDER_NAME' does not exist."
    exit 1
fi
if [ ! -f "$MAIN_PY" ]; then
    echo "Error: File 'main.py' not found in folder '$FOLDER_NAME'."
    exit 1
fi
if [ -z "$TXT_FILE" ]; then
    echo "Error: No 'rosalind_*.txt' file found in folder '$FOLDER_NAME'."
    exit 1
fi

cat "$TXT_FILE" | python3 "$MAIN_PY" >"$OUT_TXT"
