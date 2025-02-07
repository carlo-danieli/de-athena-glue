import json 
from pprint import pprint as pp
# Open the JSON file
with open('kagglehub/datasets/oftomorrow/herokuapp-makeup-products/versions/333/products.json', 'r') as file:
    data = json.load(file)

# Write each JSON object on a new line
with open('kagglehub/datasets/oftomorrow/herokuapp-makeup-products/versions/333/products_reformatted.json', 'w') as outfile:
    for item in data:
        json.dump(item, outfile)
        outfile.write('\n')