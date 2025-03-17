import json
json_file_path = "C:\\Users\\jorge\\OneDrive\\Desktop\\Cowdataset\\keypoints.json"
with open(json_file_path, 'r') as f:
    data = json.load(f)

# Extract relevant data related to cowss
cow_data = {
    "images": {},
    "annotations": [],
    "categories": []
}
cow_images = {}
cow_category_id = 5  # Assuming the category ID for cows is 5
for category in data.get('categories', []):
    if category['id'] == cow_category_id:
        cow_data['categories'].append(category)
for annotation in data.get('annotations', []):
    if annotation['category_id'] == cow_category_id:
        cow_data['annotations'].append(annotation)
for annotation in cow_data['annotations']:
    image_id = annotation['image_id']  
    images = data.get('images', {})
    if str(image_id) in images:
        image_filename = images[str(image_id)]
        cow_images[image_id] = image_filename

cow_data['images'] = cow_images

cleaned_json_file_path = "C:\\Users\\jorge\\OneDrive\\Desktop\\Cowdataset\\cleaned_keypoints_cow.json"
with open(cleaned_json_file_path, 'w') as f:
    json.dump(cow_data, f)
