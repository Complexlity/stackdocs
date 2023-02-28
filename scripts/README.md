# What Scripts ?

This folder contains scripts which was used in automatically making changes across all quest and campaign(`index.mdx`) files.

# Requirements

1. Linux terminal running on bash installed
2. `jq` package installed (Conditional. Only `addToLabel.sh` and `updatePosition.sh` require this package). Go to the [docs](https://linuxhint.com/bash_jq_command/) to learn how to install the package

# How To Use

In the root of the project folder, run `bash scripts/<script-name>`

e.g

```
// root folder
bash scripts/updatePosition.sh
```
