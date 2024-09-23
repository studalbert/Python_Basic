# TODO здесь писать код
text = input('Введите строку: ')
fst = text.index('h')
snd = text.rindex('h')
print('Развёрнутая последовательность между первым и последним h:', text[snd-1:fst:-1])