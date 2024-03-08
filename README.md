# ConcatenateYourGoproVideo

- ffmpeg is required to run the script.

Modify the `raw_video_root` and `dst_video_root` in `concatenate.py` to your own path.

```python
raw_video_root = "E:/DCIM/100GOPRO/"
dst_video_root = "./"
```

Then run the following command to concatenate your GoPro video.

```bash
python concatenate.py
```