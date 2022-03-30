import utils
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

vid = cv.VideoCapture('./res_test.mp4')
# vid = cv.VideoCapture('http://145.94.97.128:4747/video')

save_recording = True
project_name = 'res_test'

if save_recording:
    used_dirs = glob.glob(f'./projects/{project_name}*')
    idx = max([int(dir_name[-3:]) for dir_name in used_dirs], default=0) + 1
    frame_dir = f'./projects/{project_name}{idx:03}'
    os.mkdir(frame_dir)


imgs = []
comp_imgs = []

colors = {'green': [.5, .8, .7], 'purple': [.6, .5, .85]}
color = colors['purple']
frame_nr = 0

while vid.isOpened():
    success, img = vid.read()
    if success:
        # processed_image = utils.accentuation_pipeline(img, color, channel_weights=(1, 1, 1))
        # side_by_side = np.concatenate([img, np.stack((processed_image, processed_image, processed_image), axis=-1)], axis=1)
        cv.imshow('Frame', img)
        # imgs += [processed_image]
        # comp_imgs += [side_by_side]
        # print(processed_image.shape)

        # Press Q on keyboard to  exit
        if cv.waitKey(25) & 0xFF == ord('q'):
            break

        # if save_recording:
        #     np.save(frame_dir + f'/{frame_nr:06}.npy', processed_image)

    else:
        break

    frame_nr += 1

# utils.save(imgs)
# utils.save(comp_imgs, dir='side_by_side.mp4')
# print([utils.get_positions(img) for img in imgs])