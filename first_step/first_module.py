from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote, unquote

def check_from_excptn(url, stat_excptn):
    url = unquote(url)
    
    for excptn in stat_excptn.values():
        if(url.find(excptn, 0, -1) != -1):
            return 0
    
    if(url.find('wiki', 1, 5) != -1):
        url = 'https://ru.wikipedia.org' + url
    if(url.find('https://ru.wikipedia.org', 0, -1) != -1):
        print(url)
        

#Exception from rules
stat_excptn = {0: 'Википедия',1: 'Служебная',2: 'Категория', 3: 'Портал',4: 'Special',5: 'index'}
stat_excptn[6] = 'Шаблон'
stat_excptn[7] = 'Обсуждение'
stat_excptn[8] = 'Файл'
stat_excptn[9] = 'Проект'


page = input()
step = 1

if(page == 'Старт'):
    page = input()
    print('Step:', step)
    step += 1

    while page != 'Выход':
        page =  ' https://ru.wikipedia.org/wiki/' + quote(page)
        html = urlopen(page)
        doc = BeautifulSoup(html.read(), features = 'lxml');
        for link in doc.find_all('a'):
            url = str(link.get('href'))
            check_from_excptn(url, stat_excptn)
        page = input()
        if(page != 'Выход'):
            print('Step:', step)
            step += 1
