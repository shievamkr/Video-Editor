import moviepy.editor as mp
import os

# assign directory
sourceDirectory = r'D:\influecer videos to compress'
# destinationDirectory = 'C:\E Drive\KTT\Video\Compressed'

for filename in os.listdir(sourceDirectory):
    if(filename.find('mp4')>1):
        clip = mp.VideoFileClip(filename)
        partitioned_string = filename.partition('.')
        name = partitioned_string[0]
        print("Filename : " + str(filename)) 
        print("Height : " + str(clip.h))
        print("Width : " + str(clip.w))
        print("FPS : " + str(clip.fps))
        clip = clip.resize(width=360)
        print("Clip Resized")
        clip = clip.set_fps(20)
        print("FPS set to 20")
        clip.write_videofile(+name+".mp4", codec ="libx264")
        print("Video file written")