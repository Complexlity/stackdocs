import os
import json
import sys

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
name = sys.argv[1]

# Create the folder name
folder_name = "-".join(name.lower().split())

# Create the directory and change to it
os.makedirs(os.path.join("docs", folder_name))
os.chdir(os.path.join("docs", folder_name))

# Create the _category_.json file
category = {
    "label": name,
    "position": 2,
    "link": {
        "type": "doc",
        "id": f"{folder_name}/index"
    }
}
with open("_category_.json", "w") as f:
    json.dump(category, f, indent=2)

# Create the index.mdx file
with open("index.mdx", "w") as f:
    f.write(f"# {name}\n\n")
    f.write("_Brief Overview Goes Here_\n\n")
    f.write('import DocCardList from "@theme/DocCardList";\n\n')
    f.write("<DocCardList />\n\n")
    f.write(":::info FULL OVERVIEW ?\n\n")
    f.write('<QuestButton\n')
    f.write('  text="Go To Campaign Page"\n')
    f.write(f'  link="/docs/{folder_name}/"\n')
    f.write('/>\n\n')
    f.write(":::\n")

# # Create the three .md files
# for i in range(3):
#     file_name = f"{sys.argv[i+2].lower().replace(' ', '-')}.md"
#     with open(file_name, "w") as f:
#         f.write(f"---\nsidebar_position: {i+1}\n---\n\n")
#         f.write(f"# {sys.argv[i+2]}\n\n")
#         f.write("_Brief Overview Goes Here_\n\n")
#         f.write(":::tip Happy Learning!!\n\n")
#         f.write('<QuestButton text="Go To Quest" link="" />\n\n')
#         f.write(":::\n")

# Create the .md files
for i in range(2, len(sys.argv)):
    file_name = f"{sys.argv[i].lower().replace(' ', '-')}.md"
    with open(file_name, "w") as f:
        f.write(f"---\nsidebar_position: {i-1}\n---\n\n")
        f.write(f"# {sys.argv[i]}\n\n")
        f.write("_Brief Overview Goes Here_\n\n")
        f.write(":::tip Happy Learning!!\n\n")
        f.write('<QuestButton text="Go To Quest" link="" />\n\n')
        f.write(":::\n")