from pytube import YouTube
VideoLink = input("Enter the link:")
ytvideo = YouTube(VideoLink)

#Title of the YOUTUBE video
print("Video Title: ",ytvideo.title)
#Number of views
print("Number of views: ",ytvideo.views)
#Description
print("Description: ",ytvideo.description)

#store highest available resolution
downloadres = ytvideo.streams.get_highest_resolution()

customDownload = input("Download In Custom Directory? 1: Yes")
if customDownload == 1:
    location = input("Where To Save The Video: ") #else saves in Scripts Directory
    downloadres.download(location)
else:
    downloadres.download()
print("Downloading.....")