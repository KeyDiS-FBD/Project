import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://ru.wikipedia.org/wiki/" + input()
print(url)

req = requests.get(url)
if(req.status_code != 200):
    print("Page not found")
else:
    resource = urllib.request.urlopen(url)

    html = resource.info()
    type(html)
#html = unicode(html, "utf-8")
#print(html)
