import os
from socket import socket
os.system("clear")
os.system("CLS")
print ("\033[31m wqlcxm and FileZ present")
print ("✡↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎✞")
print ("░█████╗░██╗░░░██╗██████╗░░██████╗███████╗██████╗░")
print ("██╔══██╗██║░░░██║██╔══██╗██╔════╝██╔════╝██╔══██╗")
print ("██║░░╚═╝██║░░░██║██████╔╝╚█████╗░█████╗░░██║░░██║")
print ("██║░░██╗██║░░░██║██╔══██╗░╚═══██╗██╔══╝░░██║░░██║")
print ("╚█████╔╝╚██████╔╝██║░░██║██████╔╝███████╗██████╔╝")
print ("░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═════╝░")
print ("☯↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎↔︎✛")
print ("")
print("==============================================")
print ("┌Выберите действие")
print ("\033[35m[1] Поиск по номеру           ┇         [2] SMS BOMBER ")
print ("[3] Tutorials                 ┇         [4] DDos")
print ("[5] О проекте                 ┇         [6] Discord Start Token (by FileZ) ")
print ("[7] Установка модулей         ┇         [8] Поиск по телеграм" )
print ("[9] Показать лого             ┇         [10] Выйти")
print ("Возникли ошибки? Обращайтесь к @doxbinstyle (тг)")
select = input("└Выбрать ")
print("==============================================")
if select == '1':
    from get_number import get_number
    database_file = 'number.csv'
    search_value = input(f'[i]Введите номер телефона:')
    get_number(database_file, search_value)

elif select == '2':
    from bomber import time
    time()


elif select == '3':
    from tutorials import os

elif select =='4':
    os.system("CLS")
    print("\033[35m")
    from ddos import requests
    requests()
elif select == '5':
    print("Автора:")
    print('┌Автор: wqlcxm тг: @doxbinstyle')
    print("┃Автор: FileZ тг: FileZ_Plus")
    print("┃Канал wqlcxm - @wqlcxxmstyle")
    print("└Канал FileZ - ???")
    print("")
    print("О проекте:")
    print ("░█████╗░██╗░░░██╗██████╗░░██████╗███████╗██████╗░")
    print ("██╔══██╗██║░░░██║██╔══██╗██╔════╝██╔════╝██╔══██╗")
    print ("██║░░╚═╝██║░░░██║██████╔╝╚█████╗░█████╗░░██║░░██║")
    print ("██║░░██╗██║░░░██║██╔══██╗░╚═══██╗██╔══╝░░██║░░██║")
    print ("╚█████╔╝╚██████╔╝██║░░██║██████╔╝███████╗██████╔╝")
    print ("░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═════╝░")
    print ("Coder: wqlcxm. 2023")
    print ("Все права защищены.")
    print ("")
    print ("Спасибо:")
    print ("FileZ, за помощь в коде и бета-тестириование.")
    print ("Lilon, за поддержку проекта.")

elif select == "6":
    print("[!] Должно открытся окно, если оно не открылось, попробуйте снова.")
    from Disc import tkinter as tk 


elif select =='7':
    from install import os

elif select == "8":
    from get_telegram import get_telegram
    database_file = 'telegram.csv'
    search_value = input("[i]Введите ID аккаунта:")
    get_telegram(database_file, search_value)

elif select == "9":
    print("\033[31m░█████╗░██╗░░░██╗██████╗░░██████╗███████╗██████╗░")
    print("██╔══██╗██║░░░██║██╔══██╗██╔════╝██╔════╝██╔══██╗")
    print("██║░░╚═╝██║░░░██║██████╔╝╚█████╗░█████╗░░██║░░██║")
    print("██║░░██╗██║░░░██║██╔══██╗░╚═══██╗██╔══╝░░██║░░██║")
    print("╚█████╔╝╚██████╔╝██║░░██║██████╔╝███████╗██████╔╝")
    print("░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═════╝░")
    print("[!] ВЛ4CTb В TBONX PYKAX")

elif select == "9":
    exit

elif select == "exit":
    exit
