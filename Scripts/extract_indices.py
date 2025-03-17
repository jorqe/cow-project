import json
import numpy as np
from sklearn.model_selection import train_test_split
with open('D:\\Documents\\SChool\\Spring2024\\Reasearcg\\Posture Estimation\\final.json', 'r') as f:
    data = json.load(f)
image_paths = [entry['img_path'] for entry in data]
indices = np.arange(len(image_paths))
train_indices, test_val_indices = train_test_split(indices, test_size=0.2, random_state=42)
test_indices, val_indices = train_test_split(test_val_indices, test_size=0.5, random_state=42)
np.save('train_indices.npy', train_indices)
np.save('test_indices.npy', test_indices)
np.save('val_indices.npy', val_indices)
