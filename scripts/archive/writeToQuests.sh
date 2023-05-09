# This file copies the `go to quest` buttton (as well as a dummy text) into quest files 

# Text you want to copy into all quest files (excluding index.mdx) .

copyText='
_Brief Overview Goes Here_

:::tip Happy Learning!!

<QuestButton text="Go To Quest" />

:::

'

# Script that executes the command. 
for file in docs/**/*.md; do head -n 5 "$file" > "$file.tmp" && mv "$file.tmp" "$file" &&  echo "$copyText" >> "$file"; done

#Note: Copying starts from line 5 (which is below the header). 
#This could be modified to a higher number if in future you want to add a generic text to all quest files
# change `head -n 5 ` to `head -n <<your-line-number>>` to add it. 
#Optionally, <<your-line-number>>> could be negative which means counting from the base of the document