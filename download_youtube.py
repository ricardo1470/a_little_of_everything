#!/usr/bin/python3
""" script to download youtube videos
    - install pytube3 """


import subprocess
from pytube import YouTube

DOWNLOADS_FOLDER = './downloads'

def download_video(url, output_directory):
    yt = YouTube(url)
    highest_quality_stream = yt.streams.filter(
        progressive=True
    ).order_by(
        'resolution'
    ).desc(
    ).first(
    ).download(
        output_directory
    )

    return highest_quality_stream

def main():
    # Ask the user for the youtube video url
    url = input("Enter the YouTube video url: ")
    file_location = download_video(url, DOWNLOADS_FOLDER)
    subprocess.call(["open", file_location])

if __name__ == "__main__":
    main()