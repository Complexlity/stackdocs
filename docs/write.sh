copyText='
# Introduction

import DocCardList from "@theme/DocCardList";


<DocCardList />

:::info FULL SUMMARY?

<QuestButton text="Go To Campaign Page" />

:::

'

for dir in ./*/; do echo "$copyText" > "$dir/index.mdx"; done
