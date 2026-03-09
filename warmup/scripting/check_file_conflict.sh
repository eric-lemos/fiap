#!/bin/bash

file=$1
pattern="<<<<<<<|=======|>>>>>>>"

if [ -z "$file" ]; then
    echo "Usage: $0 '/path/to/file'"
    exit 1
fi

if [ ! -f "$file" ]; then
    echo "File '$file' does not exist."
    exit 1
fi

if grep -q -E "$pattern" "$file"; then
    echo "Conflict markers found in $file. Please resolve the conflicts before proceeding."
    exit 1
else
    echo "No conflict markers found in $file. You can proceed with the merge."
fi