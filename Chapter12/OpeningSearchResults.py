# Perform a google search and open different tab for each result
import sys
import urllib
import requests
from bs4 import BeautifulSoup
import webbrowser
# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'


query = '+'.join(sys.argv[1:])

# query = "hackernoon How To Scrape Google With Python"
# query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"

headers = {"user-agent": USER_AGENT}
resp = requests.get(URL, headers=headers)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    results = []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            results.append(item)
    numOpen = min(2, len(results))
    for i in range(numOpen):
        print('Opening', results[i]['link'])
        webbrowser.get(chrome_path).open(results[i]['link'])



#
# query = baseURL + ' '.join(sys.argv[1:])
# headers = {"user-agent" : MOBILE_USER_AGENT}
# res = requests.get(query, headers=headers)
# try:
#     res.raise_for_status()
#     if res.status_code == 200:
#
#         soup = bs4.BeautifulSoup(res.content, 'html.parser')
#         results = []
#         for g in soup.find_all('div', class_='r'):
#             anchors = g.find_all('a')
#             if anchors:
#                 link = anchors[0]['href']
#                 title = g.find('h3').text
#                 item = {
#                     "title": title,
#                     "link": link
#                 }
#             results.append(item)
#             print(results)
#     # numOpen = min(2, len(linkElems))
#     # for i in range(numOpen):
#     #     urlToOpen = baseURL + linkElems[i].get('href')
#     #     print('Opening', urlToOpen)
#     #     webbrowser.open(urlToOpen)
# except Exception as exc:
#     print("Error found: %s" % (exc))


#retrieve top search result links

#open browser tab for each result
