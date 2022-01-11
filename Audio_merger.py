import moviepy.editor as mp
from PIL import Image
from pathlib import Path
import os

# assign directory
videoDirectory = r'D:\MASHH\product video-20220107T151941Z-001\product video\picturess'

for filename in os.listdir(videoDirectory):
    if(filename.find('mp4')>1):
        partitioned_string = filename.partition('.')
        name = partitioned_string[0]
        my_clip = mp.VideoFileClip(filename).subclip(0, 25)
        audio_background = mp.AudioFileClip('theme.mp3').subclip(0,25)
        # final_audio = mp.CompositeAudioClip([my_clip.audio, audio_background])
        final_clip = my_clip.set_audio(audio_background)
        # audio = mp.AudioFileClip("theme.mp3").subclip(0,25)
        # video1 = mp.VideoFileClip(filename)
        # video = video1.subclip(0, 25)
        # final = video.set_audio(audio)
        final_clip.write_videofile(name+".mp4",codec= 'libx264')
        final_clip.ipython_display()
        # print(name)