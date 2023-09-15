#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import cv2


# In[ ]:


def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    video = cv2.VideoCapture(video_path)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_count = 0
    while True:
        ret, frame = video.read()

        if not ret:
            break

        frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)

        frame_count += 1
        progress_percent = (frame_count / total_frames) * 100
        print(f"Extracting frames: {progress_percent:.2f}%")

    video.release()
    print("Frames extraction complete.")

video_path = "/path to your desired video"
extract_frames(video_path, output_folder)


# In[ ]:


def delete_images(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)  
        if os.path.isfile(file_path):
            os.remove(file_path)

    print("Deletion complete")

image_folder = "/path to folder containing the video frames"
delete_images(image_folder)

