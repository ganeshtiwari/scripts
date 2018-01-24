#!/usr/bin/env python3

import sys
import os
from urllib.request import urlopen
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import youtube_dl


def get_video_url(query):
    """
    Returns the top video url of the youtube searhc query.
    """
    query = {'search_query': '{}'.format(query)}
    url = 'https://www.youtube.com/results?' + urlencode(query)
    response = urlopen(url)
    soup = BeautifulSoup(response.read().decode(), 'html.parser')
    for tag in soup.find_all('a', {'rel': 'spf-prefetch'}):
        video_url = 'https://youtube.com' + tag['href']
        return video_url


def download(video_url):
    """
    Donloads a music file in mp3 format.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        os.chdir('/home/gunace/Desktop')
        ydl.download([video_url])



def main():
    """
    Start.
    """
    query = sys.argv[1:]
    video_url = get_video_url(query)
    download(video_url)


if __name__ == '__main__':
    main()
