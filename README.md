Installation
Install ``pip install ffmpeg-python``
Install ``pip install pytubefix``

This is a program in download youtube videos. Currently with how YouTube efficiently streams videos using DASH, this program downloads the highest video stream and audio stream available and merges the files into a single mp4 file. The resulting file will be stored on the desktop.

Cannot naturally read codec av01 on windows. Suggested to use VLC media player

Currently uses pytubefix with ffmpeg to merge the streams.