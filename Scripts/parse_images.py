import os
import json
import shutil
image_folder = "C:\\Users\\jorge\\OneDrive\\Desktop\\Cowdataset\\images\\images"
json_file = "C:\\Users\\jorge\\OneDrive\\Desktop\\Cowdataset\\keypoints.json"

cow_images = set()
cow_file_names = set()
with open(json_file, 'r') as f:
    data = json.load(f)
    for entr in data['annotations']:
        if entr['category_id'] == 5:
            id = f"{entr['image_id']}" 
            cow_images.add(id)
    for cow in cow_images:
        if data['images'].get(cow) != None:
            cow_file_names.add(data['images'].get(cow))

for filename in os.listdir(image_folder):
    if filename not in cow_file_names:
        os.remove(os.path.join(image_folder, filename))
        print(f"Removed: {filename}")
print("Image cleansing complete.")
