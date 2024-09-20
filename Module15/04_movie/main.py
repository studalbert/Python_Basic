films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

# TODO здесь писать код
how_much = int(input('Сколько фильмов хотите добавить? '))
love_films = []

for i in range(how_much):
    film = input('Введите название фильма:')
    if film in films:
        love_films.append(film)
    else:
        print(f'Ошибка: фильма {film} у нас нет :(')

print('Ваш список любимых фильмов:', end = ' ')
for i in range(len(love_films) - 1):
    print(love_films[i], end = ', ')
print(love_films[-1])


