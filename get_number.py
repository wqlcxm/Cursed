def get_number(database_file, search_value):
    found = False

    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 0:
            phone = data[0]
            if search_value in phone:
                email = data[1]
                fio = data[2]
                birthday = data[3]

                print(f'''
                \033[31m[!]Фио: {fio}
                [!]Дата рождения: {birthday}
                [!]Телефон: {phone}
                [!]Почта: {email}
                      ''')
                found = True

    if not found:
        print('Ничего не найдено')

