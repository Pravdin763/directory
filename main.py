import Search
import show_all
import view
print('Вас приветствует телефонный справочник')


def menu():
    print()
    print('Выберите пункт меню: ')
    print('1 Добавить контакт')
    print('2 Показать все контакты')
    print('3 Поиск номера по фамилии')
    print()
    n = input('Введите число из меню: ')
    if n =='1':
        view.write_kontact()
        menu()
    elif n=='2':
        show_all.show_all_kontact()
        menu()
    elif n=='3':
        Search.search_kontact()
        menu()
    else:
        print('Вы допустили ошибку... Выберите один из вариантов: 1, 2, 3 ')
        menu()


menu()