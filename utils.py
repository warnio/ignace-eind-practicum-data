import numpy as np
import cv2 as cv
import os
import shutil
from skimage.util.shape import view_as_windows


def accentuate_color(distance):
    return -5*distance**2


def color_distance(frame, color, channel_weights=(1, 1, 1)):
    color = np.reshape(color, (1, 1, 3))
    frame = frame - color
    frame = frame ** 2
    frame = np.sum(frame * np.reshape(channel_weights,
                                      [1 for _ in frame.shape[:-1]] + [len(channel_weights)]), axis=-1) ** .5
    return frame


def normalize_colors(frame):
    return frame / 255


def filter_image(frame, filter_size=1, decay=.9, avg=True):
    side = 2 * filter_size + 1
    filter = np.ones((side, side))
    for i in range(side):
        for j in range(side):
            filter[i, j] *= decay ** (((filter_size - i) ** 2 + (filter_size - j) ** 2) ** 0.5)
    return cv.filter2D(frame.reshape(frame.shape + (1,)), -1, filter) / (np.sum(filter) if avg else 1)


def accentuation_pipeline(img, color, channel_weights=(1, 1, 1)):
    color = color[::-1]
    img = normalize_colors(img)
    distance = color_distance(img, color, channel_weights)
    img = accentuate_color(distance)
    for i in range(4):
        img = filter_image(img, decay=1., avg=False)
    img = img - np.max(img)
    img = np.exp(img)
    img = project_image_to_u8(img)
    return img


def localization_pipeline(img, color, channel_weights=(1, 1, 1)):
    return get_positions(accentuation_pipeline(img, color, channel_weights))


def save(frames, fps=30, dir='movie.mp4'):
    try:
        os.mkdir('dump')
    except FileExistsError:
        pass

    for i, frame in enumerate(frames):
        cv.imwrite(f'dump/img{i:0>5}.png', frame)
    os.system(f"ffmpeg -r {fps} -start_number 0 -i /home/sappie/PycharmProjects/DoublePendulum/dump/img%05d.png"
              f" -vcodec mpeg4 -y {dir}")
    shutil.rmtree('./dump')


def project_image_to_u8(frame):
    frame *= 255
    return frame.astype(np.uint8)


def change_colorscheme(img, conversion=cv.COLOR_BGR2RGB):
    return cv.cvtColor(img, conversion)


def get_positions(frame):
    return np.unravel_index(np.argmax(frame), frame.shape)
