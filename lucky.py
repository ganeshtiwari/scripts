#!/usr/bin/env python3

import requests
import sys
import webbrowser
import bs4
import time
from urllib.parse import urlparse, parse_qs


def main():
    """
    Opens at most five tabs in the default browser form the links found in google search of the query.
    """
    print('Googling. . . . . . . . . . ')
    res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    link_elems = soup.select('.r a')

    num_open = min(len(link_elems), 5)
    for i in range(num_open):
        url = urlparse(link_elems[i]['href'])
        query = parse_qs(url.query)
        webbrowser.open(query['q'][0])

main()