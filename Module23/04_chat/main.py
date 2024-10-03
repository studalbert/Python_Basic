# TODO здесь писать код
def correct_name():
    name = input('Введите имя пользователя: ')
    if not name.isalpha():
        print('Имя должно состоять только из букв')
        correct_name()

correct_name()

while True:
    try:
        active = int(input('1.Посмотреть текущий текст чата.\n'
                           '2.Отправить сообщение\n'))
        if active < 0 or active > 2:
            raise ValueError

        if active == 1:
            with open('chat.txt', 'r', encoding='utf-8') as chat:
                print(f'\n{chat.read()}')
        if active == 2:
            with open('chat.txt', 'a', encoding='utf-8') as chat:
                text = input('Введите сообщение: ')
                chat.write(f'{text}\n')

    except ValueError:
        print('Ошибка. Можно выбрать только 1 или 2')