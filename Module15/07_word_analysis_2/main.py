# TODO здесь писать код
word = input('Введите слово: ')
word = list(word)
counter = 0
for i in range(len(word)//2):
    if word[i] == word[-i-1]:
        counter += 1
if counter == len(word)//2:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
