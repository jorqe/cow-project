import os
import json
with open('D:\\Documents\\SChool\\Spring2024\\Reasearcg\\Posture Estimation\\cow\\cowimages-cowkeypoints\\cleaned_keypoints_cow.json', 'r') as f:
    data = json.load(f)
restructured_data = []
directory_path = r"D:\Documents\SChool\Spring2024\Reasearcg\Posture Estimation\cow\cowimages-cowkeypoints\images"

for annotation in data['annotations']:
    image_id = annotation['image_id']
    image_path = os.path.join(directory_path, data['images'][str(image_id)])

    img_width = 0
    img_height = 0

    img_boxes = [annotation['bbox']]
    img_joints = [annotation['keypoints']]

    existing_entry = next((entry for entry in restructured_data if entry['img_path'] == image_path), None)
    if existing_entry:
        existing_entry['img_boxes'].extend(img_boxes)
        existing_entry['img_joints'].extend(img_joints)
    else:
        image_info = {"img_path": image_path, "img_width": img_width, "img_height": img_height, "img_boxes": img_boxes, "img_joints": img_joints}
        restructured_data.append(image_info)

with open('prestructured_file.json', 'w') as f:
    json.dump(restructured_data, f, separators=(', ', ': '))
