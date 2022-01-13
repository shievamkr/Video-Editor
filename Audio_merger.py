# Import everything needed to edit video clips
from moviepy.editor import *
import os

# assign directory
# videoDirectory = r'D:\MASHH\product video-20220107T151941Z-001\product video\picturess'

# loading audio file
audioclip = AudioFileClip("theme.mp3").subclip(0, 25)


for filename in os.listdir(os.getcwd()):
    if(filename.find('mp4') > 1):
        partitioned_string = filename.partition('.')
        name = partitioned_string[0]

        # loading video 
        clip = VideoFileClip(filename)


        # getting only first 25 seconds
        # clip = clip.subclip(0, 25)

        # adding audio to the video clip
        videoclip = clip.set_audio(audioclip)
        
        # showing video clip
        videoclip.ipython_display()
        videoclip.write_videofile("change_"+name+".mp4")
        
