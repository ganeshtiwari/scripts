#!/usr/bin/env python3

import os
import requests
import bs4

url = 'https://xkcd.com/'
res = requests.get(url)
# print(res.text)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
rel_link = soup.select('#comic img')
print(rel_link[0].get('src'))