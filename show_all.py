# функция выводит всю информацию о контактах с новой строки
def show_all_kontact():
    print('Ваши контакты: ')
    print()
    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())
    file.close()

