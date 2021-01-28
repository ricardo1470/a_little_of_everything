#!/usr/bin/python3
""" script to download youtube videos
    - install pytube3 """


import pytube

url = 'https://www.youtube.com/watch?v=7t2o-AS-Kb0&list=RD7t2o-AS-Kb0&start_radio=1'

youtube = pytube.YouTube(url)

video = youtube.streams.get_by_itag(135)
video.download('C:/Users/cresp/Documents/bots')