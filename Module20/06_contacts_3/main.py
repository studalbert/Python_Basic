# TODO здесь писать код
phonebook = {}
def active1(name_surname, phone):
    if tuple(name_surname.split()) in phonebook:
        print('Этот человек уже есть в словаре')
    else:
        phonebook[tuple(name_surname.split())] = int(phone)
        print(phonebook)
def active2(phonebook):
    for key, value in phonebook.items():
        if key[1].title() == surname.title():
            print(key[0], key[1], value)

while True:
    num_active = int(input(f'Введите номер действия:\n1.Добавить контакт\n2.Найти человека\n'))
    if num_active == 1:
        name_surname = input('Введите имя и фамилию нового контакта (через пробел): ')
        phone = input('Введите номер телефона: ')
        active1(name_surname, phone)
    if num_active == 2:
        surname = input('Введите фамилию для поиска: ')
        active2(phonebook)