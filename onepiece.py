#!/usr/bin/env python3

import os
import sys
import requests
from pathlib import Path
from bs4 import BeautifulSoup

class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

def get_manga(url, chapter):
    try:
        res = requests.get(url)
        res.raise_for_status()
    except:
        print('error in fetching resource: {}'.format(chapter))
        return 
    
    to_dir = handle_dir(chapter)

    soup = BeautifulSoup(res.text, 'html.parser')
    
    part_url = []
    for tag in soup.select('.content-area img'):
        part_url.append(tag['src'])

    print('******* Downloading: {} to {} *******\n'.format(chapter, to_dir))

    count = 1
    for part in part_url:
        print(part)
        res = requests.get(part)
        f = open((to_dir + '/%s' + '-%s') % (chapter, count), 'wb')
        for chunk in res.iter_content(1000):
            f.write(chunk)
        count += 1

    print('\n******* Complete: {} to {} *******\n'.format(chapter, to_dir))

def handle_dir(chapter):
    if not os.path.isdir(str(Path.home()) + '/one-piece-manga'):
        os.mkdir(str(Path.home()) + '/one-piece-manga')
    
    if not os.path.isdir(str(Path.home()) + '/one-piece-manga' + '/{}'.format(chapter)):
        os.mkdir(str(Path.home()) + '/one-piece-manga' + '/{}'.format(chapter))
    to_dir = os.path.join(str(Path.home()), 'one-piece-manga', '{}'.format(chapter))

    return to_dir

def _main():
    chapter = sys.argv[1]
    url = 'https://manga-fox.com/one-piece/chapter-{}'.format(chapter)
    get_manga(url, chapter)

if __name__ == '__main__':
    _main()
