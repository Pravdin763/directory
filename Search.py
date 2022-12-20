# Функция ведет поиск по фамилии, если есть - выводит все данные. Если нет -выводит сообщение...
def search_kontact():
    n = input('Введите фамилию контакта: ')
    with open('file.txt', 'r', encoding='utf-8') as file:
        kontact =''
        for i in file:
            x = i.split()[1]
            if n.title() in x:
                kontact = i
        if kontact != '':
            print(kontact)
        else:
            print('Такой фамилии нет в вашем списке контактов..')
            search_kontact()
        file.close()


