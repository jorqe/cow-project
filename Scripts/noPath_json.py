import json

with open('D:\\Documents\\SChool\\Spring2024\\Reasearcg\\Posture Estimation\\cow\\jsonfiles\\final.json', 'r') as f:
    data = json.load(f)

prefix_to_remove = "D:\\Documents\\SChool\\Spring2024\\Reasearcg\\Posture Estimation\\cow\\cowimages-cowkeypoints\\images\\"
for entry in data:
    entry['img_path'] = entry['img_path'].replace(prefix_to_remove, "")
with open('noPath_final.json', 'w') as f:
    json.dump(data, f, separators=(', ', ': '))
