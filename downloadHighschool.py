import os 
import youtube_dl


def hande_download(urls, count):
    ydl_opts = {}

    for url in urls:
        video_name = url.split('/')[-1].split('.')[0]
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            os.chdir('/home/gunace/Videos/highschool/s2/')
            ydl.download([url])
            os.rename('{}-{}.{}'.format(video_name, video_name, 'mp4'), '{}.mp4'.format(count))
            count += 1


def main():
    urls = [
            'https://www435.playercdn.net/185/2/U4W8ELkQD9jrtYy_HgrCTg/1527841687/180215/842FOHQAP34MCHRLSRRTN.mp4',
            'https://www2418.playercdn.net/185/1/-BZgTf_mG0Z1ZLYpQsHYsA/1527841746/180215/839FOHQ6JDFVIRSHOTPNE.mp']
    count = 311
    hande_download(urls , count)

main()