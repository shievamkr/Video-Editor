import moviepy.editor
import os

# assign directory
videoDirectory = r'C:\Users\shiva\OneDrive\Desktop\git repo\Video-Editor'

for filename in os.listdir(videoDirectory):
    if (filename.find('mp4') > 1):
        partitioned_string = filename.partition('.')
        name = partitioned_string[0]    #extracting name of the file
        video=moviepy.editor.VideoFileClip(filename) #converting video to AUDIO
        audio=video.audio
        audio.write_audiofile(name+".mp3")  #renaming file name 
        print(name)
