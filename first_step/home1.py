#Поиск в Русской википедии, Если есть статья с таким названием

import urllib.request import urlopen                    #открыть или загрузить файлы через http
import requests                                         #отправить http запрос
from urllib.parse import quote

name = input()
url = "https://ru.wikipedia.org/wiki/" + quote(name)    #Единный адрес страницы
req = requests.get(url)                                 #отправили http запрос, вся информация теперь хранится в объекте Response
if(req.status_code != 200):                             #код состояния запроса
    print('Page Not Found')
else:           
    resource = urllib.request.urlopen(url)              #открывает соединение с URL-адресом
    f = open(name + '.html', 'wb')                      #открыть файл для записи в бинарном формате
    f.write(resource.read())                            #запись в файл
    f.close()                                           #закрiыть файл
