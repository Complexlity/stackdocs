copyText='
# Introduction

import DocCardList from "@theme/DocCardList";


<DocCardList />

:::info SEE FULL SUMMARY

<QuestButton text="Got To Campaign Page" link='' />

:::

'

for dir in ./*/; do echo "$copyText" > "$dir/index.mdx"; done
