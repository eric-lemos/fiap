#!/bin/bash

function check_file_conflicts() {
    local file="$1"
    local pattern="<<<<<<<|=======|>>>>>>>"

    if grep -q -E "$pattern" "$file"; then
        echo "Conflict markers found in $file. Please resolve the conflicts before proceeding."
    fi
}

function check_dir_conflicts() {
    local dir="$1"
    for item in "$dir"/*; do
        if [ -f "$item" ]; then
            check_file_conflicts "$item"
        elif [ -d "$item" ]; then
            check_dir_conflicts "$item"
        fi
    done
}

dir=$1

if [ -z "$dir" ]; then
    echo "Usage: $0 '/path/to/directory'"
    exit 1
fi

if [ ! -d "$dir" ]; then
    echo "Directory '$dir' does not exist."
    exit 1
fi

check_dir_conflicts "$dir"