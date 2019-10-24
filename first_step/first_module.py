from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote, unquote

#def print_another_letters(str word)


name = quote(input())
html = urlopen("https://ru.wikipedia.org/wiki/" + name)
doc = BeautifulSoup(html.read(), features = 'lxml');
for link in doc.find_all('a'):
    word = str(link.get('href'))
    if(word.find('wiki', 1, 5) != -1):
        word = unquote(unquote('https://ru.wikipedia.org' + word))
        print(word)
    elif(word.find('https://ru.wikipedia.org', 0, -1) != -1):
        word = unquote(unquote(word))
        print(word)
