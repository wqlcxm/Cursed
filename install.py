import os

print("\033[33mОбновление python-pip...\033[0m")
os.system("pip install --upgrade pip")
print("")
bib = ["html5lib", "phonenumbers", "requests", "bs4",  "urllib3", "sys", "folium", "threading", "time", "random", "datetime", "argparse", "colorama", "tkinter", "base64"]
for i in range(len(bib)):
    print("\033[33mУстановка "+bib[i]+"...\033[0m")
    os.system("pip install "+bib[i])
print('\033[32mУстановка завершена!\033[0m')
