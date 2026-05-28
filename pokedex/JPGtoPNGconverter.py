import sys
import os
from PIL import Image

# grab first and second argument
source = sys.argv[0]
destination = sys.argv[1]

# check if new/ exists, if not create it
if not os.path.isdir(destination):
  os.mkdir(destination)

# loop through Pokedex,
# convert images to png
# save to the new folder
for root, dirs, files in os.walk(source):
  for file in files:
    img = Image.open(f'{source}{file}')
    clean_name = os.path.splitext(file)[0]
    img.save(f'{destination}/{clean_name}', 'png')