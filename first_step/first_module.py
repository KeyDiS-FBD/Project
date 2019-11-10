from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote, unquote
import requests
#Exception from rules

def check_response_code(page):
    response = requests.get(page)
    code = response.status_code
    if(code != 200):
        print('Not found or other problems, code of response:', code)
        return 1
    return 0


def parsing_site(page):
    dict_of_excptn = {0 : 'Википедия', 1 : 'Служебная', 2 : 'Категория', 3 : 'Портал', 4 : 'Special', 5 : 'index', 6 : 'Шаблон', 7 : 'Обсуждение', 8 : 'Файл', 9 : 'Проект'}
    excptn_cntr = 10
    html = urlopen(page)
    doc = BeautifulSoup(html.read(), features = 'lxml');        #BeautifulSoup for parsing html file
        
    for link in doc.find_all('a'):
        url = str(link.get('href'))
        flag = 0                                                #flag for exceptions 
        if(url.find('wiki', 1, 5) != -1):                       #if the link is relative
            url = 'https://ru.wikipedia.org' + url
            
        url = unquote(url)                                      #unquote for decrypt url
            
        for excptn in dict_of_excptn.values():
            if((url.find(excptn, 0, -1) != -1) or (excptn == url)):
                flag = 1
            
        if((url.find('https://ru.wikipedia.org', 0, -1) != -1) and (flag != 1)):
            print(url)
            dict_of_excptn.setdefault(excptn_cntr, url)         #add temporary exceptions
            excptn_cntr += 1 
        
    for i in range(excptn_cntr - 1, 9, -1):                     #remove all temporary exceptions
        dict_of_excptn.pop(i, )
    return 0

rules = open('rules.txt')
print(rules.read())

page = input()
step = 1
if(page == 'Старт'):
    while(page != 'Выход'):
        page = input()
        page =  'https://ru.wikipedia.org/wiki/' + quote(page)     #quote for encrypt input in url
        if(check_response_code(page)):
            break;
        else:
            print('Step:', step)
            parsing_site(page)

        step += 1

