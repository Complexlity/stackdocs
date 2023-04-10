import os
import json
import sys
import re

def format_input_string(input_string):
    # Replace all & with and
    input_string = input_string.replace('&', 'and')
    # Replace all special characters with " " and trim consecutive spaces to a single space
    # input_string = re.sub(r'[^\w\s:;]+', ' ', input_string).strip()
    input_string = re.sub(r'[^\w\s]|_', ' ', input_string)
    # Convert everything to lower case
    input_string = input_string.lower()
    # Replace all spaces with (-) excluding spaces occurring at the end or beginning of the text
    input_string = '-'.join(input_string.split())
    # Return the formatted string
    return input_string

# This updates the position property of the _category_.json files so the new campaign would be added at the top of the sidebar
for root, dirs, files in os.walk('docs'):
    for file in files:
        if file == '_category_.json':
            filepath = os.path.join(root, file)
            with open(filepath, 'r+') as f:
                data = json.load(f)
                data['position'] += 1
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()


# Get the name from the command line argument
campaign_name = sys.argv[1]

# Remove special characters and replace '&' with 'and'
campaign_name_formatted = format_input_string(campaign_name)
print(campaign_name_formatted)
# Create the folder name from the full name of the campaign
campaign_folder_name = "-".join(campaign_name_formatted.lower().split())
print(campaign_folder_name)

# Create the directory and change to it
campaign_folder_path = os.path.join("docs", campaign_folder_name)
os.makedirs(campaign_folder_path)
os.chdir(campaign_folder_path)

# Create the _category_.json file for the new campaign folder
category = {
    "label": campaign_name,
    "position": 2,
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
        f.write(f"---\nsidebar_position: {i-1}\n---\n\n")
        f.write(f"# {sys.argv[i]}\n\n")
        f.write("_Brief Overview Goes Here_\n\n")
        f.write(":::tip Happy Learning!!\n\n")
        f.write('<QuestButton text="Go To Quest" link="" />\n\n')
        f.write(":::\n")