# This script takes the label from _category_.json and makes it the header of `index.mdx` in each folder

for file in ./**/*.mdx; do
  label=$(jq -r '.label' "${file%/*}/_category_.json")
  sed -i "1s/.*/# $label\n\n_Brief Overview Goes Here_/" "$file"
done