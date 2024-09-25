violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

# TODO здесь писать код
songs_count = int(input('Сколько песен выбрать? '))
result = 0
for i in range(songs_count):
    songs_name = input(f'Название {i+1} песни: ')
    result += violator_songs.get(songs_name, 0)

print(f'Общее время звучания песен: {result:.2f} минуты')