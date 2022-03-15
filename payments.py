
from SimpleQIWI import *#Для работы с API QIWI
from time import sleep#Для таймера
from random import randint#Рандомайзер
import requests#Для работы с запросами
import json#Для расшифровки json


def receipt():
    api_access_token = 'a6c894l3b7e5470084700226001c06е50045e4177dd' # токен можно получить здесь https://qiwi.com/api
    phone = "88888888888"

    coment = str(randint(100000, 999999))
    suma = 5

    print(f"Переведите {suma} рублей на QIWI счет'{phone}'\n С коментарием: {coment}")

    tir = 0
    for i in range (12):#Главный цикл
        if tir == 1:#Проверяем можем ли остановить цикл
            break

        s = requests.Session()
        s.headers['authorization'] = 'Bearer ' + api_access_token  
        h = s.get('https://edge.qiwi.com//payment-history/v2/persons/88888888888/payments?rows=3&operation=IN&sources%5B0%5D=QW_RUB&sources%5B1%5D=CARD ')
        a = json.loads(h.text)#В переменной хранится информация о переводах в виде словаря в котором можно копатся

        f = 0
        for i in range (3):#второй цикл

            #Вытаскивам из переменной то что нам нужно
            dd = a['data']
            ss = dd[f]#Вытаскиваем конкретный элемент (инф. об одном платеже)
            aa = ss['comment']#Вытаскиваем коментарий прикреплённый к платежу
                    
            #Вытаскиваем сумму
            aa1= ss['sum']
            aa2 = aa1['amount']

            #Проверяем коментарий
            if aa == coment:#Проверяем коментарий 
                if aa2 == suma:#Проверяем сумму
                    print("Платёж прошёл успешно")
                    print(aa)#Выводим коментарий


                    tir = 1#Говорим что пора выключать главный цикл ибо цель достигнута
                    break
                                      
            f = f + 1#Меняем значение переменной чтоба с каждой итерацией второго цикла брать новый элемент переменной "a" (инф. о следующем платеже)
             
        if tir == 0:#Это нужно чтобы после того как оплата пройдёт не ждать 20 секунд и остановить цикл
            print(20)
            time.sleep(20)#ждём 20секунд и снова вытаскиваем информацию о платежах
receipt()

   












