import cv2
import numpy as np
from pathlib import Path
import os
import matplotlib.pyplot as plt
import tqdm
from datetime import date

def im2vid(data, name):

    print(f'{data}')

    data = f'{data}'
    image_list = os.listdir(data)
    image_list.sort()

    # Find shape 
    first_image = cv2.imread(f'{data}/000001.jpg') # replace and figure out how to extract first mage automatically !! 
    height, width, layers = first_image.shape

    # Writing the output video

    #today = date.today()
    #today = today.strftime("%m-%d-%Y")
    output_path = f'{data}/{name}.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 30
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for count, file in tqdm.tqdm(enumerate(image_list), total = len(image_list)):

        image_path = os.path.join(data, file)
        im = cv2.imread(image_path)
        video_writer.write(im) # write the frame to the video file

    video_writer.release()
    print(f'Video saved at {output_path}')

def vid2im(source_path, output_path):
    video_capture = cv2.VideoCapture(source_path)
    
    frame_number = 0

    while True: 
        ret, frame = video_capture.read()

        if not ret: 
            break

        output_filename = os.path.join(output_path, f'{frame_number+1:06}.jpg')
        cv2.imwrite(output_filename, frame)

        frame_number += 1

    video_capture.release()


#vid2im('/home/ubuntu/.cache/pypoetry/virtualenvs/boxmot-2v5TJBaT-py3.10/Archangel_car.mp4', '/home/ubuntu/.cache/pypoetry/virtualenvs/boxmot-2v5TJBaT-py3.10/Archangel_car')

im2vid('/home/ubuntu/.cache/pypoetry/virtualenvs/boxmot-2v5TJBaT-py3.10/boxmot/runs/track/Archangel_deepocsort2', 'Archangel_deepsort')