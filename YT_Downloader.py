import pytube

def download(type):
    try:
        if type == 'v':
            video = youtube.streams.filter(resolution='1080p').first()
            video.download("./Pobrane/Video")

       # if type == 'm':
            #music


    except:
        print("Something went wrong! Try again!")
    finally:
        print("Your file was downloaded!")

# video_url = input("Paste video url: ")
video_url = 'https://www.youtube.com/watch?v=FWDXwrgdm9w'
youtube = pytube.YouTube(video_url)

song_info = youtube.title
artist = song_info.lower().find("-")

if song_info.lower().find("(official video)") == -1:
    official_video = len(song_info)

else:
    official_video = song_info.lower().find("(official video)")

print("Artist: {}".format(song_info[0:artist - 1]))
print("Song name: {}".format(song_info[artist + 2:official_video + 1]))
print("Link do grafiki z podglądu: {}".format(youtube.thumbnail_url))
print("-------------------")
music_video = input("Do you wanna download video(v) / music(m)? ")
download(music_video)
