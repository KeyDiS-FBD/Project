from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote

name = quote(input())
html = urlopen("https://ru.wikipedia.org/wiki/" + name)
doc = BeautifulSoup(html.read(), features = 'lxml');
for link in doc.find_all('a'):
    word = str(link.get('href'))
    if(word.find('wiki', 1, 5) != -1):
        print('https://ru.wikipedia.org' + word)
    elif(word.find('https://ru.wikipedia', 0, -1) != -1):
        print(word)
