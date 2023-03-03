import os
import json

folders = os.listdir('docs')

for folder in folders:
    if folder[0].isdigit():
        num = int(folder[0]) + 1
        new_name = f"{num}{folder[1:]}"
        os.rename(os.path.join('docs', folder), os.path.join('docs', new_name))
        category_path = os.path.join('docs', new_name, '_category_.json')
        with open(category_path, 'r+') as f:
            category = json.load(f)
            category['position'] += 1
            f.seek(0)
            json.dump(category, f, indent=2)
            f.truncate()
