import requests
import os
import bs4
import threading
os.makedirs('xkcd', exit_ok=True)


def downloadxkcd(start_comic, end_comic):
    for url_num in range(start_comic, end_comic):
        print('Downloading page https://xkcd.com/%s----' % (url_num))
        res = requests.get('http://xkcd.com/%s' % (url_num))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        comic_elem = soup.select('#comic img')

        if comic_elem == []:
            print('Could not find comic image.')
        else:
            comic_url = comic_elem[0].get('src')
            