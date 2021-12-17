from pytube import YouTube

#where to save
SAVE_PATH = "D:/video scrappimg" #to_do

#link of the video to be downloaded
link=open('links_file.txt','r')

for i in link:
	try:
		
		# object creation using YouTube
		# which was imported in the beginning
		yt = YouTube(i)
		video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
		print(i)
	except:
		
		#to handle exception
		print("Connection Error")
		continue
	
	#filters out all the files with "mp4" extension
	

	# get the video with the extension and
	# resolution passed in the get() function
	# video = yt.streams.first() 
	try:
		# downloading the video
		video.download(SAVE_PATH)
	except:
		print("Some Error!")
  
print('Task Completed!')
