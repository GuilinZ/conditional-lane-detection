import cv2
import os
import tqdm
import re
path = './vis_out/'
file_names = [name for name in os.listdir(path) if ('gt' not in name)]
file_names.sort(key=lambda f: int(re.sub('\D', '', f)))
vid_writer = cv2.VideoWriter('./out.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 60, (1920, 1080))
for name in tqdm.tqdm(file_names):
    if 'gt' in name:
        continue
    frame = cv2.imread(path+name)
    vid_writer.write(frame)