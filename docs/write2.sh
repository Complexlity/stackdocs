copyText='
_Summary Goes Here_

:::tip Happy Learning!!

<QuestButton text="Go To Quest" />

:::

'

for file in ./**/*.md; do head -n 5 "$file" > "$file.tmp" && mv "$file.tmp" "$file" &&  echo "$copyText" >> "$file"; done
