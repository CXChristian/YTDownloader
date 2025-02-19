import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from pytubefix import YouTube
import ffmpeg
import os
import re

DESKTOP_PATH =      os.path.join(os.path.expanduser("~"), "Desktop")
SAVE_FINAL_PATH =   f'{DESKTOP_PATH}\\YTDownloads'
SAVE_PART_PATH =    f'{SAVE_FINAL_PATH}\\temp'
TYPE_DOWNLOAD =     "mp4"
VIDEO =             "video"
AUDIO =             "audio"

class MainWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        
        # Window Settings
        self.setWindowTitle("YT Downloader")
        self.setGeometry(700, 300, 600, 500)
        self.setWindowIcon(QIcon("icon.jpg"))
        
        # Top Banner Label
        label = QLabel("Welcome to YT Downloader!", self)
        label.setGeometry(0, 0, 600, 50)
        label.setFont(QFont('Arial', 30))
        label.setStyleSheet("color: #363130;"
                            "background-color: #bababa;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        label.setAlignment(Qt.AlignCenter)
    
        # Line edit component
        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(50, 100, 500, 50)
        self.line_edit.setStyleSheet("font-size: 20px;"
                                     "font-family: Arial")
        self.line_edit.setPlaceholderText("Enter link of video")

        # Button component
        self.button = QPushButton("Download", self)
        self.button.setGeometry(200, 150, 200, 50)
        self.button.setStyleSheet("font-size: 20px;"
                                  "font-family: Arial")
        self.button.clicked.connect(self.submit)
        
        # Window Downloader
        self.downloader = Downloader()

    def submit(self):
        text = self.line_edit.text()
        print(f"Entered: {text}")
        self.downloader.run(text)

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

def clean_string(text):
    # Define a regular expression pattern to match special characters
    pattern = re.compile(r'[^\w\s]', re.UNICODE)
    cleaned_text = pattern.sub('', text)
    print(f"Cleaned Title: {cleaned_text}")
    return cleaned_text

def console_launch():
    downloader = Downloader()
    print(f"Final Path: {SAVE_FINAL_PATH}")
    unselected = True
    while (unselected):
        print("Welcome to YT Downloader!")
        print("Type 'exit' to exit the program")
        link = input("Enter the link of the video you want to download: ")

        if (link == "exit"):
            exit()

        downloader.run(link)
        unselected = False

def window_launch():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

def main():
    # Window Version
    # window_launch()

    # Console Version
    console_launch()

if __name__ == "__main__":
    main()