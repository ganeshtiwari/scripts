import os
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from pprint import pprint
import threading


def get_url(url):
    response = requests.get(url)
    html_doc = response.text

    wallpaper_urls = []
    soup = BeautifulSoup(html_doc, 'html.parser')
    for tag in soup.find_all(class_='wallpaper_pre'):
        wallpaper_urls.append('https:' + tag.a['href'])

    raw_image_urls = get_image_url(wallpaper_urls)
    # pprint(raw_image_urls)
    image_urls_dict = parse_image_urls(raw_image_urls)
    # pprint(image_urls_dict)

    to_dir = handle_dir()

    threads = []
    for name, image_url in image_urls_dict.items():
        download_thread = threading.Thread(target=download_image, args=[name, image_url, to_dir], daemon=True)
        threads.append(download_thread)
        download_thread.start()

    for thread in threads:
        thread.join()


def get_image_url(urls):
    image_urls = []
    print('******* Getting root image  urls *******')

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        raw_url = soup.find(class_='wb_preview').a['href']
        image_urls.append(raw_url)

    return image_urls


def parse_image_urls(raw_image_urls):
    image_urls_dict = {}
    print('******* Parsing urls *******')
    for url in raw_image_urls:
        split_list = url.split('/download/')
        key_list =split_list[-1].split('/')
        image_urls_dict[key_list[0]] = 'https://wallpaperscraft.com/image/' + '_'.join(key_list) + '.jpg'

    return image_urls_dict


def download_image(name, url, to_dir):
    response = requests.get(url)
    print('\nDownloading {}'.format(url))
    f = open((to_dir + '/{}').format(name + '.jpg'), 'wb')
    for chunk in response.iter_content(1000):
        f.write(chunk)


def handle_dir():
    if not os.path.isdir(str(Path.home()) + '/Pictures' + '/anime'):
        os.mkdir(str(Path.home()) + '/Pictures' + '/anime')

    to_dir = os.path.join(
        str(Path.home()) + '/Pictures' + '/anime')

    return to_dir


def main():
    url_list = "https://wallpaperscraft.com/catalog/anime/page14" 
        # "https://wallpaperscraft.com/catalog/anime/page15" 
        # "https://wallpaperscraft.com/catalog/anime/page16"
        # "https://wallpaperscraft.com/catalog/anime/page17"
    # ]
    for base_url in url_list:
        thread = threading.Thread(target=get_url, args=[url_list], daemon=True)
        thread.start()
        thread.join()



if __name__ == '__main__':
    main()