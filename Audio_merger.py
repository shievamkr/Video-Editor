# Import everything needed to edit video clips
from moviepy.editor import *
from pathlib import Path
import os

# assign directory
videoDirectory = r'D:\MASHH\product video-20220107T151941Z-001\product video\picturess'

for filename in os.listdir(videoDirectory):
    if(filename.find('mp4')>1):
        partitioned_string = filename.partition('.')
        name = partitioned_string[0]
        output = name +".mp4"
        
        clip = VideoFileClip(filename)


        # getting only first 5 seconds
        clip = clip.subclip(0, 25)

        # loading audio file
        audioclip = AudioFileClip("theme.mp3").subclip(0,25)

        # adding audio to the video clip
        videoclip = clip.set_audio(audioclip)
        videoclip.write_videofile(output,codec ="vp9")
        # showing video clip
        videoclip.ipython_display()
