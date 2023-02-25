for file in ./**/*.md; do head -n -6 "$file" > "$file.tmp" && mv "$file.tmp" "$file" && cat ./copy2.txt >> "$file"; done
