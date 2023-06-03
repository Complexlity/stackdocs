import os
import json
import sys
import re

def format_input_string(input_string):
    # Replace all '&' with 'and'
    input_string = input_string.replace('&', 'and')

    # replace all special characters with " " and trim consecutive spaces to a single space
    input_string = re.sub(r'[^\w\s]|_', ' ', input_string)

    # Convert everything to lower case
    input_string = input_string.lower()

    # Replace all spaces with (-) excluding spaces occurring at the end or beginning of the text
    input_string = '-'.join(input_string.split())

    # Return the formatted string
    return input_string


# Find the json file with the name highest_position.json and get the value of "highest" property
with open('docs/highest_position.json', 'r') as f:
    data = json.load(f)
    current_highest_position = data['highest']

new_highest_position = current_highest_position + 1

# Get the name from the command line argument
campaign_name = sys.argv[1]

# Remove special characters and replace '&' with 'and'
campaign_name_formatted = format_input_string(campaign_name)

# Create the folder name from the full name of the campaign
campaign_folder_name = "-".join(campaign_name_formatted.lower().split())


# Create the directory and change to it
campaign_folder_path = os.path.join("docs", campaign_folder_name)
try:
    # Try to change to the directory
    os.chdir(campaign_folder_path)
except FileNotFoundError:
    # If the directory doesn't exist, create it
    os.makedirs(campaign_folder_path)
    os.chdir(campaign_folder_path)

# Create the _category_.json file for the new campaign folder
category = {
    "label": campaign_name,
    "position": new_highest_position,
    "link": {
        "type": "doc",
        "id": f"{campaign_folder_name}/index"
    }
}
with open("_category_.json", "w") as f:
    json.dump(category, f, indent=2)

# Create the index.mdx file
with open("index.mdx", "w") as f:
    f.write(f"# {campaign_name}\n\n")
    f.write("_Brief Overview Goes Here_\n\n")
    f.write('import DocCardList from "@theme/DocCardList";\n\n')
    f.write("<DocCardList />\n\n")
    f.write(":::info FULL OVERVIEW ?\n\n")
    f.write('<QuestButton\n')
    f.write('  text="Go To Campaign Page"\n')
    f.write(f'  link=""')
    f.write('/>\n\n')
    f.write(":::\n")

# Create the .md files for each quest
for i in range(2, len(sys.argv)):
    input_string_formatted = format_input_string(sys.argv[i])
    # Add ".md" to the end of the file name
    quest_file_name = input_string_formatted + '.md'
    with open(quest_file_name, "w") as f:
        sidebar_position = len(sys.argv) - i
        f.write(f"---\nsidebar_position: {sidebar_position}\n---\n\n")
        f.write(f"# {sys.argv[i]}\n\n")
        f.write("_Brief Overview Goes Here_\n\n")
        f.write(":::tip Happy Learning!!\n\n")
        f.write('<QuestButton text="Go To Quest" link="" />\n\n')
        f.write(":::\n")

#Update the position.json and give the 'highest' property the value of current_highest_position
with open('../highest_position.json', 'w') as f:
    data['highest'] = new_highest_position
    json.dump(data, f, indent=2)

# Update the sidebar_position property in welcome.mdx
with open('../welcome.mdx', 'r+') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if 'sidebar_position' in lines[i]:
                lines[i] = f'sidebar_position: {new_highest_position + 1}\n'
    f.seek(0)
    f.writelines(lines)
    f.truncate()