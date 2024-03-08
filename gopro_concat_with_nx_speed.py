import subprocess
from time import sleep
import os, sys

raw_video_root = "E:/DCIM/100GOPRO/"
dst_video_root = "./"

video_idx = input("last 4 number of the video (xxxx-xxxx or xxxx): ").strip().replace("\n", "")
speed = input("speed (0.5, 1.0, 2.0, ...): ").strip().replace("\n", "")
video_output_name = input("video output name: ").strip().replace("\n", "")

file_all = os.listdir(raw_video_root)
video_set = {}

if "-" in video_idx:
    video_idx = video_idx.split("-")
elif video_idx == "q":
    sys.exit(0)
else:
    video_idx = [video_idx, video_idx]
video_idx = [x for x in range(int(video_idx[0]), int(video_idx[1])+1)]

for file in file_all:
    if not int(file[4:8]) in video_idx:
        continue
    name_temp = file[:2] + str(video_idx[0])
    if not name_temp in video_set:
        video_set[name_temp] = []
    video_set[name_temp].append(file)

for key in video_set:
    with open(f"videolist_{key}.txt", "w") as f:
        for file in video_set[key]:
            f.write(f"file '{raw_video_root}{file}'\n")

# concat videos
for key in video_set:
    if speed == "1.0":
        subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", f"videolist_{key}.txt", "-c", "copy", f"{dst_video_root}{video_output_name}.mp4"])
    else:
        subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", f"videolist_{key}.txt", "-filter:a", f'atempo={speed}', f"{dst_video_root}{video_output_name}.mp4"])
    sleep(1)

# rm videolist.txt
for key in video_set:
    os.remove(f"videolist_{key}.txt")


