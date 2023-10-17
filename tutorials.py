import os
os.system("clear")
os.system("CLS")
print ("░█████╗░██╗░░░██╗██████╗░░██████╗███████╗██████╗░")
print ("██╔══██╗██║░░░██║██╔══██╗██╔════╝██╔════╝██╔══██╗")
print ("██║░░╚═╝██║░░░██║██████╔╝╚█████╗░█████╗░░██║░░██║")
print ("██║░░██╗██║░░░██║██╔══██╗░╚═══██╗██╔══╝░░██║░░██║")
print ("╚█████╔╝╚██████╔╝██║░░██║██████╔╝███████╗██████╔╝")
print ("░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═════╝░")
print("__________Author: wqlcxm__________________________")
print("____________________________Tutorial______________")
print("Здесь будут туториалы по темам, которые не смогли внести в скрипт.")
print("")
print("[!] Выберите туториал")
print("[1.] Узнать админа сообщества вк через gif")
print("[2.] Как деанонить и где распостранить информацию")
print("[3.] Сервисы для создания временных почт")
print("[4.] Удаленние мета-данных с фотографий")
print("[5.] Вернутся в тулл")

select = input("")
print("==================================================")
if select == '1':
    print("Итак, для начала нам нужно любое вк сообщество.")
    print("Моим примером будет: https://vk.com/doska_pozora08")
    print("Нажимаем на знак лупы и в строку пишем \"gif\"")
    print("Когда нашли гифку от сообщества открываем её в новой вкладке.")
    print("Теперь удаляем из ссылки все лишнее.")
    print("Пример:")
    print("До: https://vk.com/doc2000061618_650274065?hash=VdawilN5UeZzWpcktd3t0hzELDZsg8Z07RQbmkb7oBz&dl=VcOV1l5lpye0mvMmh9mSdfFnQxCUdLp6sSBzXbBdwww")
    print("После: https://vk.com/doc2000061618")
    print("Далее заменяем /doc на /id и переходим по этой ссылке.")
    print("Вот и всё! Теперь у вас есть страница вк автора сообщества и его можно деанонить.")

if select == '2':
    print("Чтобы деанонить нам нужно найти инфу о человеке.")
    print("Инфу можно найти как-раз через наш тулл.")
    print("Далее заходим на сайт doxbin.net и регистрируемся там.")
    print("Нажимаем на \"Add Paste\"")
    print("В появшиеся перед нами строки мы можем вставить информацию о человеке.")
    print("Далее выкладываем её и всё.")

if select == '3':
    print("Temp Mail (www.temp-mail.org)")
    print("Guerrilla Mail (www.guerrillamail.com)")
    print("10 Minute Mail (10minutemail.com)")
    print("Mailinator (www.mailinator.com)")
    print("Fake Mail Generator (www.fakemailgenerator.com)")
    print("YopMail (www.yopmail.com)")
    print("MailDrop (www.maildrop.cc)")
    print("Tempail (www.tempail.com)")
    print("ThrowAwayMail (www.throwawaymail.com)")
    print("Dispostable (www.dispostable.com)")  

if select == "4":
    print("1. Перейдите на веб-сайт \"Online Metadata Removal Tool\" по ссылке: https://www.exifpurge.com/.")
    print("2. На главной странице вы увидите кнопку \"Выберите файл\" или \"Drag & Drop\" (перетащите файлы для удаления метаданных).")
    print("3. Щелкните на кнопке \"Выберите файл\", чтобы выбрать фотографию или перетащите фотографию непосредственно на веб-сайт.")
    print("4. После выбора файла сервис начнет удаление метаданных с фотографии.")
    print("5. По завершении удаления метаданных, вы получите возможность скачать очищенную фотографию обратно на свой компьютер.")

if select == "5":
    from Kills import os