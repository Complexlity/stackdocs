# What Scripts ?

This folder contains scripts which was used in automatically making changes accross all quest files and `index.mdx` files.

# Requirements

1. Linux terminal running on bash installed
2. `jq` package installed (Conditional. Only `addToLabel.sh` and `updatePosition.sh` require this package). Go to the [docs](https://linuxhint.com/bash_jq_command/) to learn how to install the package

# How To Use

1. Copy the particular script into `/docs` folder
2. Run `cd docs` (enters the folder on the terminal)
3. Run `bash <script-name>`

e.g

```
// /docs
bash updatePosition.sh
```
