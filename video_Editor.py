from moviepy.editor import VideoFileClip
from PIL import Image
#from pathlib import Path
import os

# assign directory
videoDirectory = 'C:\Users\shiva\OneDrive\Desktop\Video'

for filename in os.listdir(videoDirectory):
    if(filename.find('m4v')>1):
        partitioned_string = filename.partition('.')
        name = partitioned_string[0]
        clip = VideoFileClip(filename)
        frame = clip.get_frame(1) # Gets a numpy array representing the RGB picture of the clip at time frame_at_second
        new_image = Image.fromarray(frame) # convert numpy array to image
        new_image.save(name+".jpg") # save the image
        clip = clip.subclip(0, 4)
        clip = clip.resize(0.14)
        clip.write_gif(name+".gif", fps=5)
        print(name)