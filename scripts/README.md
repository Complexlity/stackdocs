# What Scripts ?

This folder contains scripts which was used in automatically making changes across all quest and campaign (`index.mdx`) files.

# Bash Scripts

These are those ending with `.sh`

## Requirements

1. Linux terminal running on bash installed
2. `jq` package installed (Conditional. Only `addToLabel.sh` and `updatePosition.sh` require this package). Go to the [docs](https://linuxhint.com/bash_jq_command/) to learn how to install the package

## How To Use

In the root of the project folder, run `bash scripts/<script-name>`

e.g

```
// root folder
bash scripts/updatePosition.sh
```

Refer to each script file to see what it is doing

# Python Scripts

This is for script(s) ending with `.py`

## Requirements

1. Python 3 installed on the machine
   Follow the guides below

- [How to install python 3 on linux](https://docs.python-guide.org/starting/install3/linux/)
- [How to install linux on windows](https://phoenixnap.com/kb/how-to-install-python-3-windows)

## createCampaign.py

This script as the name implies is used to create a new campaign and quest files in one go.

### How to use

It takes at least two **required** command line arguments.
The first must be the full title of the campaign to be added
The other arguments are the full title of the quests under it

In the root folder, run the command

```
python3 scripts/createCampain.py "<campaing name>" "<quest one name>" "<quest two name>" ....
```

This can take a many arguments as you pass. So run it according to how many quest are under the new campaign.
