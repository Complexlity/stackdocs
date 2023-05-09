# This file copies the `go to campaign` button into all `index.mdx` files

# Text you want to copy into all index files
copyText='
# Introduction

import DocCardList from "@theme/DocCardList";


<DocCardList />

:::info FULL OVERVIEW ?

<QuestButton text="Go To Campaign Page" />

:::

'


# Script that runs
for dir in docs/*/; do echo "$copyText" > "$dir/index.mdx"; done
