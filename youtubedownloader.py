from pytube import YouTube


savepath='/home/kalesh/Desktop'

link = "https://www.youtube.com/watch?v=60ItHLz5WEA"

try:
    # object creation using YouTube which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error")  # to handle exception

# filters out all the files with "mp4" extension
mp4files = yt.filter(progressive=True, file_extension='mp4')


yt.set_filename('python downloaded')  # to set the name of the file

# get the video with the extension and resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
try:
    # downloading the video
    d_video.download(savepath)
except:
    print("Some Error!")

print('Task Completed!')