from pytubefix import YouTube
import ffmpeg
import os

SAVE_FINAL_PATH =   f'{os.path.expanduser("~")}/Desktop/YTDownloads'
SAVE_PART_PATH =    f'{SAVE_FINAL_PATH}/temp'
TYPE_DOWNLOAD =     "mp4"
VIDEO =             "video"
AUDIO =             "audio"

def download_part(yt, type):
    try:
        if (type == VIDEO):
            ys = yt.streams.filter(file_extension=TYPE_DOWNLOAD)[1]
            print(f'Video Streams: {ys}')
        elif (type == AUDIO):
            ys = yt.streams.filter(file_extension=TYPE_DOWNLOAD, type=AUDIO)[1]    
            print(f'Audio Streams: {ys}')
            
        ys.download(output_path=SAVE_PART_PATH)
        print("Part Downloaded!")
    except:
        print("Could Not Find Stream!")

def merge_mp4(title):
    try:
        video_path = f'{SAVE_PART_PATH}/{title}.mp4'
        audio_path = f'{SAVE_PART_PATH}/{title}.m4a'
        output_path = f'{SAVE_FINAL_PATH}/{title}.mp4'

        video_ffmpeg = ffmpeg.input(video_path)
        audio_ffmpeg = ffmpeg.input(audio_path)
        ffmpeg.output(video_ffmpeg, audio_ffmpeg, output_path, vcodec='copy', acodec='copy').run()

        print("Video and audio combined successfully!")
    except:
        print("Error combining video and audio!")

def clean_temp(title):
    try:
        os.remove(f'{SAVE_PART_PATH}/{title}.mp4')
        os.remove(f'{SAVE_PART_PATH}/{title}.m4a')
        print("Temp files removed!")
    except:
        print("Could not remove temp files!")

unselected = True
while (unselected):
    print("Welcome to YT Downloader!")
    print("Type 'exit' to exit the program")
    link = input("Enter the link of the video you want to download: ")

    if (link == "exit"):
        exit()

    try:
        yt = YouTube(link)
        print(yt.title)
        unselected = False
    except:
        print("Connection Error")
        print("Try Again")

download_part(yt, VIDEO)
download_part(yt, AUDIO)

merge_mp4(yt.title)

clean_temp(yt.title)