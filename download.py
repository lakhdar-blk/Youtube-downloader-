import pytube

def download(url, location, type_file):

    youtube = pytube.YouTube(url)
    
    try:

        if(type_file == "Audio"):
            video = youtube.streams.filter(only_audio=True).first()
        elif(type_file == "Video"):
            video = youtube.streams.filter(file_extension="mp4").first()
        
        video.download(location)
        
        return 1

    except:
        
        return 0

    