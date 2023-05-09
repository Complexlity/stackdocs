
import os
import json

# Load highest_position.json and get the current_highest_position value
with open('docs/highest_position.json', 'r') as f:
    data = json.load(f)
    current_highest_position = data['highest']

# Walk the entire docs and reverse the position values in _category_.json files
for root, dirs, files in os.walk('docs'):
    for file in files:
        if file == '_category_.json':
            filepath = os.path.join(root, file)
            with open(filepath, 'r+') as f:
                data = json.load(f)
                data['position'] = current_highest_position - data['position'] + 2
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()

# Update the sidebar_position property in welcome.mdx
with open('docs/welcome.mdx', 'r+') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if 'sidebar_position' in lines[i]:
            lines[i] = f'sidebar_position: {current_highest_position + 1}\n'
    f.seek(0)
    f.writelines(lines)
    f.truncate()