import random as r
def exam_num(num):          # функция проверяет правильно ли введен номер
    if num[0] == '8' and len(num) == 11 and num.isdigit() == True:
        return num
    else:
        print('Вы допустили ошибку, введите номер еще раз: ')
        exam_num(input())

def num_input():            # Функция предлагает ввести номер вручную или автоматически сгенерировать его
    print('Выберите вариант ввода')
    var = int(input('1 Ввести номер вручную   2 Ввести номер автоматически: '))
    if var == 1:
        number = input('Введите телефон через 8: ')
        num = exam_num(number)
        return num
    elif var == 2:
        num = str(r.randrange(89000000000, 90000000000))
        return num
    else:
        print("Вы ввели не правильный символ, введите 1 или 2")
        num_input()

def write_kontact():            # Функция создает контакт
    with open('file.txt', 'a', encoding='utf-8') as file:
        director = []
        name = input('Введите имя: ').title()
        surname = input('Введите фамилию: ').title()
        number = num_input()

        com = input('Введите комметнарий (Необязательно): ').title()
        director.append(name)
        director.append(surname)
        director.append(number)
        if len(com) > 0:
            director.append(com)
        director = ' '.join(director)
        file.write(director)
        file.write('\n')
        file.close()
