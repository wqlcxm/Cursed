def get_telegram(database_file, search_value):
    found = False

    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 0:
            id = data[0]
            if search_value in id:
                phone = data[1]
                last_name = data[2]
                first_name = data[3]

                print(f'''                                             
                [!]ID: {id}
                [!]Возможная фамилия: {last_name}
                [!]Возможное имя: {first_name}
                [!]Телефон: {phone}
                      ''')
                found = True

    if not found:
        print(f'Ничего не найдено')

