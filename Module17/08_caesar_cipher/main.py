# TODO здесь писать код
text = input('Введите текст: ')
shift = int(input('Введите сдвиг: '))
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
result = ''
for sym in text:
  if sym in alphabet:
    result += alphabet[(alphabet.index(sym) + shift) % len(alphabet)]
  else:
    result += sym
print(result)
