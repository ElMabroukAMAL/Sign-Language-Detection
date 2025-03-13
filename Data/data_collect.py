import os
import cv2
import uuid
import time

# Path to psave the collected images
image_path = "CollectedImages"

# Sign activities to collect
labels = ['Hello', 'Yes', 'No', 'Thanks', 'IloveYou', 'Please']

# Number of images to collect per label
num_images = 20

for label in labels:

    #CREATE FOLDERS & READ THE CAMERA

    img_path = os.path.join(image_path, label)
    os.makedirs(img_path, exist_ok=True)
    # Open the camera (0 : use the laptop camera ifelse give the ID of the camera)
    cap = cv2.VideoCapture(0)
    print(f"Collecting images for {label}")
    time.sleep(5)

    #COLLECT THE IMAGES
    
    for img_num in range(num_images):
        #read the frame 
        success, frame = cap.read()
        #unique ID for each image
        image_name = os.path.join(f"{label}_{str(uuid.uuid1())}.jpg")
        #save the image 
        cv2.imwrite(os.path.join(img_path, image_name), frame)
        #to see the window ( named 'frame')
        cv2.imshow('frame', frame)
        time.sleep(1)

        # to stop the camera (press q)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

    cap.release()