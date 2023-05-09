import os
import re

# Step 1: Go into the docs folder
docs_folder = 'docs'
os.chdir(docs_folder)

# Step 2: Iterate over subfolders in docs folder
for root, dirs, files in os.walk('.'):
    # Step 2.1: Count the files and subtract 2
    total_positions = len(files) - 2

    # Step 2.2: Iterate over .md files in the subfolder
    for file in files:
        if file.endswith('.md'):
            # Step 3: Change sidebar_position in each .md file
            file_path = os.path.join(root, file)
            with open(file_path, 'r+') as f:
                content = f.read()
                # Find the sidebar_position value using regex
                match = re.search(r'sidebar_position:\s*(\d+)', content)
                if match:
                    sidebar_position = int(match.group(1))
                    new_sidebar_position = total_positions - sidebar_position + 1
                    # Replace the sidebar_position value
                    updated_content = re.sub(r'sidebar_position:\s*\d+', f'sidebar_position: {new_sidebar_position}', content)
                    f.seek(0)
                    f.write(updated_content)
                    f.truncate()
