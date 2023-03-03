#!/bin/bash

cd docs

for folder in */; do
    folder_name=$(echo "${folder%/}" | cut -d '.' -f 2-)
    mv "$folder" "$folder_name"
done
