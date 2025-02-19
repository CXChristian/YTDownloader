import os
from pytubefix import YouTube
import ffmpeg
from utils import clean_string

DESKTOP_PATH =      os.path.join(os.path.expanduser("~"), "Desktop")
SAVE_FINAL_PATH =   f'{DESKTOP_PATH}\\YTDownloads'
SAVE_PART_PATH =    f'{SAVE_FINAL_PATH}\\temp'
TYPE_DOWNLOAD =     "mp4"
VIDEO =             "video"
AUDIO =             "audio"

class Downloader():
    def run(self, input):
        try:
            yt = YouTube(input)
            print(yt.title)
            
            self.download(yt, VIDEO)
            self.download(yt, AUDIO)

            # Cleans title for file name usage
            clean_title = clean_string(yt.title)
            self.merge_mp4(clean_title)

            self.clean_temp(clean_title)
        except:
            print("Run process failed!")
 
    """
    This is the function to download the video and audio from a YouTube video.
    The function takes in the YouTube object and the type of download (video or audio).
    Windows will not allow special characters to be used in file names, so we need to clean the title.
    """
    def download(self, yt, type):
        try:
            if (type == VIDEO):
                ys = yt.streams.filter(file_extension=TYPE_DOWNLOAD)[1]
                print(f'Video Streams: {ys}')
                clean_filename = f'{clean_string(yt.title)}.mp4'
            elif (type == AUDIO):
                ys = yt.streams.filter(file_extension=TYPE_DOWNLOAD, type=AUDIO)[1]    
                print(f'Audio Streams: {ys}')
                clean_filename = f'{clean_string(yt.title)}.m4a'
 
            ys.download(output_path=SAVE_PART_PATH, filename=clean_filename)
            print("Part Downloaded!")
        except:
            print("Could Not Find Stream!")

    def merge_mp4(self, title):
        # ys.download remove special characters for file name
        try:
            video_path = f'{SAVE_PART_PATH}\{title}.mp4'
            audio_path = f'{SAVE_PART_PATH}\{title}.m4a'
            output_path = f'{SAVE_FINAL_PATH}\{title}.mp4'

            video_ffmpeg = ffmpeg.input(video_path)
            audio_ffmpeg = ffmpeg.input(audio_path)
            ffmpeg.output(video_ffmpeg, audio_ffmpeg, output_path, vcodec='copy', acodec='copy').run()

            print("Video and audio combined successfully!")
        except:
            print("Error combining video and audio!")

    def clean_temp(self, title):
        try:
            os.remove(f'{SAVE_PART_PATH}\{title}.mp4')
            os.remove(f'{SAVE_PART_PATH}\{title}.m4a')
            print("Temp files removed!")
        except:
            print("Could not remove temp files!")