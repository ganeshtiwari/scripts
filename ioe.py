from bs4 import BeautifulSoup
import requests

def get_url(site_url):
    ls = []
    response = requests.get(site_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        url = link.get('href')
        if url:
            if url.startswith('/Images/'):
                yield(site_url + url)



def main():
    site_url = 'https://exam.ioe.edu.np'
    res = get_url(site_url)
    for item in res:
        print(item)

if __name__ == '__main__':
    main()
