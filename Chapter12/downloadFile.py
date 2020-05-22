#Using requests module to donwload file from web

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')


try:
    #always call raise_for_status() after a call to requests.get
    res.raise_for_status()
    playFile = open('RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()
except Exception as exc:
    print("Error found: %s" % (exc))
