# Cow Pose Estimation

## Overview

This project aims to develop a computer vision system for accurately detecting and estimating the posture of cows in images. The system leverages the YOLO (You Only Look Once) object detection framework along with keypoint detection techniques. The goal is to infer various postures of cows by identifying their skeletal keypoints.

This system has potential applications in precision livestock farming, where monitoring cattle health and behavior is crucial. The project explores the training, evaluation, and deployment of a YOLO-based model, as well as data augmentation techniques to improve the model's robustness.

## Table of Contents

1. [Overview](#overview)
2. [Introduction](#introduction)
3. [Dataset](#dataset)
4. [Implementation](#implementation)
   - [Data Preprocessing](#data-preprocessing)
   - [Model Training](#model-training)
5. [Evaluation and Testing](#evaluation-and-testing)
6. [Future Work](#future-work)
7. [Contributing](#contributing)

##Introduction

### Purpose
The cow pose estimation project aims to provide a computer vision system for monitoring and analyzing the posture and movements of cattle in agricultural settings. By using advanced computer vision techniques, this project seeks to enhance livestock welfare, optimize farm management, and support agricultural research and innovation.

### Intended Audience
This project is intended for:
- Researchers and agricultural scientists working on livestock management
- Computer vision, machine learning, and AI professionals interested in agricultural applications
- Students and enthusiasts exploring interdisciplinary studies at the intersection of technology and agriculture

### Project Scope
The project involves:
- Data collection and annotation
- YOLO model training and evaluation
- Deployment of the trained model for real-world applications
- Data augmentation and model optimization

## Dataset

The dataset used for this project includes animal pose annotations across five categories: cows, dogs, cats, horses, and sheep. The dataset contains over 6,000 instances across 4,000 images, with annotations stored in JSON format. The annotations include 20 keypoints, such as the eyes, nose, ears, elbows, and knees.

For this project, the focus is on cows. The dataset was filtered to only include cow-related annotations and corresponding images.

### Example of Original JSON Format
```json
{
  "images": {
    "1": "image1.jpg",
    "2": "image2.jpg"
  },
  "annotations": [
    {
      "image_id": 1,
      "bbox": [123, 115, 379, 275],
      "keypoints": [[193, 216, 1], [160, 217, 1], ...],
      "num_keypoints": 20,
      "category_id": 1
    }
  ],
  "categories": [
    {
      "supercategory": "animal",
      "id": 1,
      "name": "Cow",
      "keypoints": ["left_eye", "right_eye", "nose", ...],
      "skeleton": [[0, 1], [0, 2], ...]
    }
  ]
}
```

## Implementation

### Data Preprocessing

1. **Dataset Filtering**:
   - Initially, the dataset contained images of various animals such as cows, dogs, cats, horses, and sheep.
   - The dataset was filtered to include only the annotations related to cows.
   - This reduced the total number of images from around 4,000 to 500.

2. **JSON Parsing**:
   - The annotations for the dataset were stored in JSON format, where each image had an associated set of keypoints.
   - The parsing process involved extracting keypoint data, bounding boxes, and ensuring that the keypoints corresponded to the correct parts of the cow (e.g., eyes, nose, ears).

3. **Keypoint Extraction**:
   - Keypoints were extracted for the cow's body parts such as the eyes, ears, shoulders, knees, and hooves.
   - The dataset provided 20 keypoints for each cow instance.

4. **Reformatting for YOLO**:
   - The next step involved converting the annotations from the original JSON format into the format required by YOLO.
   - This format included bounding box data and the positions of the 20 keypoints in a specific format compatible with YOLO's detection algorithm.

### Model Training

1. **Model Selection**:
   - The YOLO (You Only Look Once) framework was chosen due to its ability to perform both object detection and keypoint localization efficiently in real-time.
   - YOLO was trained using the filtered cow dataset with annotations reformatted into the required format for YOLO.

2. **Configuring YOLO**:
   - The YOLO configuration files were updated to match the cow pose estimation task. This included modifying the number of classes (to represent cows), as well as adjusting anchor boxes and image sizes.

3. **Training the Model**:
   - The model was trained using a combination of the cow images and annotations.
   - A few training techniques were implemented, such a and early stopping, to ensure the model trained efficiently and prevented overfitting. Through training I saw that anything over 60 epoch starting provided declining results
   
4. **Data Augmentation**:
   - To improve the model's generalization in the future, data augmentation strategies were planned but not yet employed, including:
     - **Flipping**: Horizontally flipping images to simulate different camera angles.
     - **Rotation**: Slightly rotating images to simulate natural movement.
     - **Scaling**: Random scaling of images to account for different cow sizes.
     - **Color Jittering**: Adjusting brightness and contrast to simulate varying lighting conditions.

---

## Evaluation and Testing

- The model’s performance was evaluated using standard metrics like Mean Average Precision (mAP), as well as loss metrics such as box_loss (for bounding box accuracy) and pose_loss (for keypoint accuracy).
- During training, the train.box_loss and train.pose_loss values were monitored to track how well the model was learning to localize objects and predict keypoints. Similarly, val.box_loss and val.pose_loss were used to evaluate the model on the validation set and gauge its ability to generalize.
- While the model showed progress, the accuracy in detecting cows and estimating their poses was still not fully determined. Further analysis of these loss values will be necessary to understand the model’s strengths and areas for improvement, particularly in challenging scenarios like occlusion or varying lighting conditions.
---

##Future Work

- **Model Improvement**: We plan to further optimize the model by experimenting with different architectures such as YOLOv4 or YOLOv5, which could provide better accuracy and speed.
- **Real-Time Deployment**: We aim to deploy the model in a real-time environment for farm monitoring applications, allowing farmers to track the behavior and health of cattle.
- **Multiclass Support**: The model could be expanded to support multiple animal classes, enabling it to estimate poses for a wider range of livestock.
- **Advanced Data Augmentation**: Implementing more advanced augmentation techniques like synthetic data generation or using GANs (Generative Adversarial Networks) to create diverse training data.

---

## Contributing

At this time, this project is **not open for contributions**. However, feel free to use the code and provide feedback. 

Thank you for your interest!

If you would like to get in touch, please reach out via [LinkedIn](https://www.linkedin.com/in/rojo-jorge/).


THANKYOU FOR YOUR INTEREST!!!!!!!

---
