# Traffic-Sign-Detection

## Project Overview

**Detection and classification of traffic signs in real-time.**  
I used the YOLOv5 large object detection algorithm to achieve accurate and efficient results.

## Steps in the Project

1. **Data Augmentation:**  
   I started with 18,000 images which I augmented to create 55,000 images across 20 classes.  
   The Python code for augmentation can be found in the file [augmentation_code.py](augmentation_code.py).

2. **Dataset Splitting:**  
   I created three datasets: train, val and test.
![Numarul de poze pentru fiecare clasa](https://github.com/user-attachments/assets/f68799e4-a9d0-4e8f-a12f-39fbbf1c7bff)

3. **Creating `dataset.yaml`:**  
   I created a `dataset.yaml` file which specifies the paths to the datasets and the classes.  
   The YAML configuration will be utilized in the Python code [dataset.yaml](dataset).

4. **Creating `.txt` Files:**  
   For each image, I created corresponding `.txt` files containing annotation data.  
   You can find the Python script for this process [here](creare_txt).

5. **Random Function for Data:**  
   A random function was used to ensure the proper distribution of images in train, val, and test sets.  
   You can view the Python code for this function [here](functia_random).

6. **Downloading YOLO Model:**  
   The YOLOv5 model was downloaded for training.  
   You can download the model from the [Ultralytics YOLOv5 GitHub repository](https://github.com/ultralytics/yolov5).

7. **Training the Model:**  
   The model was trained using the YOLOv5 Large (L) version, and the training process took approximately 9 hours.
   
### Sample Images
![image](https://github.com/user-attachments/assets/3a06b738-2fa7-4c65-9828-beb3c0aa75da)
![image](https://github.com/user-attachments/assets/3948e658-b7fc-4929-90d7-c51cfb2a8b7a)
![image](https://github.com/user-attachments/assets/cb0a9ba8-add4-4995-9fa5-789c4914850c)
![image](https://github.com/user-attachments/assets/208f4a55-715f-4afb-af39-0b03f1ce1834)
![image](https://github.com/user-attachments/assets/d35c5a9c-f159-488f-bfff-9ab7fee845a7)
![image](https://github.com/user-attachments/assets/a3babb24-1c06-434d-914c-03a4436a0720)


### Real-Time Video




