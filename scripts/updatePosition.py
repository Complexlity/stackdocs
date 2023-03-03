import os
import json

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
