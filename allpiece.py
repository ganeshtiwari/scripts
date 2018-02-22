#!/usr/bin/env python3

import sys
import time
from testpiece import get_manga

def handle_download(chapter):
    url = 'https://manga-fox.com/one-piece/chapter-{}'.format(chapter)
    get_manga(url, chapter)
        

def _main():    
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    for chapter in range(start, end + 1):
        print('Initiating Donwnload from chapter {}\n'.format(chapter))
        try:
            handle_download(chapter)
            time.sleep(1)
        except KeyboardInterrupt:
            sys.exit(1)
                
_main()