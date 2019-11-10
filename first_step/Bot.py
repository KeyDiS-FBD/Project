from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote, unquote
import telebot
import requests


bot = telebot.TeleBot('1001322227:AAF60A1WS4k41SS7CrQMxrFC5Oc4DLRVo3w')

rules = open('rules.txt')

def check_response_code(page):
    response = requests.get(page)
    if(response.status_code != 200):
        return 1
    return 0


@bot.message_handler(content_types = ['text'])

def send_rules(message):
    if(message.text == '/rules'):
        rul = rules.read()
        bot.send_message(message.chat.id, rul)
    else:
        send_results(message)


def send_results(message):
    page = message.text
    
    #Exception from rules
    
    dict_of_excptn = {0 : 'Википедия', 1 : 'Служебная', 2 : 'Категория', 3 : 'Портал', 4 : 'Special', 5 : 'index', 6 : 'Шаблон', 7 : 'Обсуждение', 8 : 'Файл', 9 : 'Проект'}
    excptn_cntr = 10
    page =  ' https://ru.wikipedia.org/wiki/' + quote(page)     #quote for encrypt input in url
    if(check_response_code(page)):
        bot.send_message(message.chat.id, 'Страница не найдена, либо существует ошибка')
        return 0
        


    html = urlopen(page)
    if(html.getcode() != 200):
        bot.send_message(message.chat.id, 'Страница не существует')
    else:
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
                bot.send_message(message.chat.id, url)
                dict_of_excptn.setdefault(excptn_cntr, url)         #add temporary exceptions
                excptn_cntr += 1 
        
        for i in range(excptn_cntr - 1, 9, -1):                     #remove all temporary exceptions
            dict_of_excptn.pop(i, )

bot.polling(none_stop = True, interval = 0)                     #wait message 
