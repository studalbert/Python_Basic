# TODO здесь писать код
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print(f'Сейчас на вечеринке {len(guests)} человек')
    guest = input('Гость пришёл или ушёл? ')
    if guest == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    name_guest = input('Имя гостя: ')
    if guest == 'пришел' and len(guests) != 6:
        print('Привет', name_guest)
        guests.append(name_guest)
    elif guest == 'пришел' and len(guests) == 6:
        print(f'Прости, {name_guest}, но мест нет.')
    elif  guest == 'ушел' and name_guest in guests:
        print('Пока', name_guest)
        guests.remove(name_guest)
    elif guest == 'ушел' and name_guest not in guests:
        print('Такого гостя нет')