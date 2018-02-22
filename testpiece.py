#!/usr/bin/env python3

import os
import sys
import requests
import threading
import time
import logging
from pathlib import Path
from bs4 import BeautifulSoup

logging.basicConfig(filename='log/onepiece.log', level=logging.ERROR)

lock = threading.Lock()

count = 0

def get_manga(url, chapter):
    try:
        res = requests.get(url)
        res.raise_for_status()
    except KeyboardInterrupt:
        sys.exit(2)
    except:
        logging.error('{}'.format(chapter))
        return

    to_dir = handle_dir(chapter)

    soup = BeautifulSoup(res.text, 'html.parser')

    part_url = []
    for tag in soup.select('.content-area img'):
        part_url.append(tag['src'])

    if len(part_url) < 3:
        print('Not updated')
        sys.exit(1)

    print('******* Downloading: {} *******'.format(chapter))

    thread_list = []
    for part in part_url:
        thread = threading.Thread(target=handle_download, args=[
                                  part, to_dir, chapter], daemon=True)
        thread_list.append(thread)
        thread.start()
    print('Found {} pages\n'.format(threading.active_count()))
    time.sleep(1)
    print('Initiating {} connections\n'.format(threading.active_count()))

    for thread in thread_list:
        thread.join()
        global count
        count = 0


def handle_dir(chapter):
    if not os.path.isdir(str(Path.home()) + '/one-piece-manga'):
        os.mkdir(str(Path.home()) + '/one-piece-manga')

    if not os.path.isdir(str(Path.home()) + '/one-piece-manga' + '/{}'.format(chapter)):
        os.mkdir(str(Path.home()) + '/one-piece-manga' + '/{}'.format(chapter))
    to_dir = os.path.join(
        str(Path.home()), 'one-piece-manga', '{}'.format(chapter))

    return to_dir


def handle_download(part, to_dir, chapter):
    global count
    lock.acquire()
    try:
        count += 1
        f = open((to_dir + '/%s' + '-%s') % (chapter, count), 'wb')
    finally:
        lock.release()

    res = requests.get(part)
    for chunk in res.iter_content(1000):
        f.write(chunk)


def _main():
    chapter = sys.argv[1]
    url = 'https://manga-fox.com/one-piece/chapter-{}'.format(chapter)
    get_manga(url, chapter)


if __name__ == '__main__':
    _main()
