# process division into split frames
import glob
import cv2
import numpy as np
import utils

split_dir = '/eind-practicum/videos/VID_20220325_130317_split'
videos = glob.glob(split_dir + '/*.mp4')

colors = {'green': [.5, .8, .7], 'purple': [.6, .5, .85]}
color = colors['purple']


def process_video(frames):
    pass

def sub_split_video(video_file_name, parts: int=200):
    imgs = []
    vid = cv2.VideoCapture(video_file_name)
    success, image = vid.read()
    while success:
        imgs.append(image)
        success, image = vid.read()
        if len(imgs) >= parts:
            imgs = np.stack(imgs, axis=0)

            positions = [utils.accentuation_pipeline(img, color, channel_weights=(1, 1, 1)) for img in imgs]

            print(imgs.shape)
            imgs = []

for video in videos:
    process_video(video)
