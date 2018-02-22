import requests
from threading import Thread
import sys
from queue import Queue

count = 0

def get_url():
    for i in range(100000):
        yield 'https://wrc.edu.np'

def doWork():
    while True:
        url = q.get()
        status, url = getStatus(url)
        doSomethingWithResult(status, url)
        q.task_done()

def getStatus(ourl):
    try:
        # print(ourl)
        res = requests.get(url)
        global count
        count += 1
        res.raise_for_status()
        return res.status_code, ourl
    except:
        return "error", ourl

def doSomethingWithResult(status, url):
    print(url + ' : ' +  str(status) + ' : ' + str(count))

concurrent = 200
q = Queue(concurrent * 2)

for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    for url in get_url():
        # print(url)
        q.put(url.strip())
    q.join()
except KeyboardInterrupt:
    sys.exit(1)