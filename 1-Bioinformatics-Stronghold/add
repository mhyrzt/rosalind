#!/bin/bash
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <number> <string-with-spaces>"
    exit 1
fi
number=$1
input_string=$2
formatted_string=$(echo "$input_string" | tr ' ' '-')
directory_name="${number}-${formatted_string}"
mkdir -p "$directory_name"
touch "${directory_name}/main.py"
