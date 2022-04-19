# split videos using ffmpeg
import ffmpeg
import cv2
import os
import glob

vid_dir = '/home/sappie/PycharmProjects/DoublePendulum/eind-practicum/videos/VID_20220325_140328.mp4'

video = ffmpeg.input(vid_dir)
# video.output('edited_side_by_side.mp4').run()

def get_frame_count(vid_dir):
    cap = cv2.VideoCapture(vid_dir)
    return int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

def split_video(vid_dir, frame_per_vid=1000):
    frame_count = get_frame_count(vid_dir)
    print(f'{frame_count} frames in video')
    # create a new directory for the split videos
    new_dir = vid_dir.split('.')[0] + '_split'
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)

    progress = glob.glob(new_dir + '/*')
    progress = max([int(x.split('/')[-1].split('.')[0]) for x in progress], default=0)
    progress = 0

    # split the video into frames
    vid = ffmpeg.input(vid_dir)
    for i in range(progress, frame_count, frame_per_vid):
        # save the new video
        new_vid = vid.trim(start_frame=i, end_frame=i+frame_per_vid).setpts('PTS-STARTPTS')
        new_vid.output(new_dir + '/' + str(i) + '.mp4').run()


split_video(vid_dir)