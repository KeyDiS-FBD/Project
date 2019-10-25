from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote, unquote

def push_in_dict(exception, url):
    pass

def check_n_print(url, exception):
    url = unquote(url)
    for i in exception.keys():
        if(url.find(exception[i], 0, -1) != -1):
            return
    if(url.find('wiki', 1, 5) != -1):
        url = 'https://ru.wikipedia.org' + url
        
    if(url.find('https://ru.wikipedia.org', 0, -1) != -1):
        print(url)

        

#Exception from rules
exception = {0: 'Википедия',1: 'Служебная',2: 'Категория', 3: 'Портал',4: 'Special',5: 'index'}
exception[6] = 'Шаблон'
exception[7] = 'Обсуждение'
exception[8] = 'Файл'
exception[9] = 'Проект'


name = input()
step = 1

if(name == 'Старт'):
    print('Step:', step)
    step += 1
    name = input()
    while name != 'Выход':
        name = quote(name)
        html = urlopen("https://ru.wikipedia.org/wiki/" + name)
        doc = BeautifulSoup(html.read(), features = 'lxml');
        for link in doc.find_all('a'):
            url = str(link.get('href'))
            check_n_print(url, exception)
        print('Step:', step)
        step += 1
        name = input()


