import os
import json
from PIL import Image
def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        return img.size
with open('D:\\Documents\SChool\\Spring2024\\Reasearcg\\Posture Estimation\\noPath_file.json', 'r') as f:
    data = json.load(f)

for entry in data:
    img_path = entry['img_path']
    img_width, img_height = get_image_dimensions(img_path)
    entry['img_width'] = img_width
    entry['img_height'] = img_height
with open('noPath_final.json', 'w') as f:
    json.dump(data, f, separators=(', ', ': '))
