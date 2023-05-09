#ARCHIVED: This file is no longer used. It's functions have been re-written. See createCampaign.py

# This file update's the 'position' property in all _category_.json files

for file in docs/**/_category_.json; do
  new_pos=$(jq '.position + 1' "$file")
  sed -i "s/\"position\":.*/\"position\": $new_pos,/" "$file"
done

#IMPORTANT: I you want to add a new campaign to the docs, ensure you run this command first before creating the folder

