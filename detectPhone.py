#!/usr/bin/env python
# coding: utf-8

# # Import librairies


import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2
import time
import os


# # With OpenCV read cam and detect phone with yolov5

# Define the fonction 
def video(outPath='vid/',):
    """
    outPath : The path where we will save the vid
    """
    outPath += str(time.time())+".avi"
    model = torch.hub.load('ultralytics/yolov5', 'yolov5l', pretrained=True)
    cap = cv2.VideoCapture(0)
    currentFrame = 0
    # Get current width of frame
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # float
    # Get current height of frame
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(outPath, fourcc,9, (int(width), int(height)))
    phone_detect = False
    # When it arrive we play a sound to say that the program is running
    with open('common/init', 'w') as fp:
        pass
    prev_frame_time = 0
    new_frame_time = 0
    while cap.isOpened():
        ret, frame = cap.read()
        # Make detection
        results = model(frame)
        analyse = results.pandas().xyxy[0]
        phone_detect = "cell phone" in analyse['name'].unique()
        if phone_detect:
            files = os.listdir("common/")
            create_read = "read" in files
            if create_read == False:
                with open('common/read', 'w') as fp:
                    pass
        new_frame_time = time.time()
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time
        fps = int(fps)
        fps = str(fps)
        fps = str(fps)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('YOLO',np.squeeze(results.render()))
        # Saves for video
        out.write(frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            with open('common/quit', 'w') as fp:
                pass
            break
        currentFrame += 1
        time.sleep(0.05)
        phone_detect = False
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video()