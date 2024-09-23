# TODO здесь писать код
text = input('Введите текст: ')
letters = "аоиеёэыуюя"
result = [x for x in text if x in letters]
print('Список гласных букв:', result)
print('Длина списка:', len(result))