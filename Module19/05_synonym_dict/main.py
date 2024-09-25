# TODO здесь писать код
words_num = int(input('Введите количество пар слов: '))
synonym_dict = dict()
for i in range(words_num):
    synonym_dict[f'{i+1} пара'] = input(f'{i+1} пара: ')
# print(synonym_dict)

while True:
    flag = True
    word = input('Введите слово: ')
    for value in synonym_dict.values():
        result = value.lower().split(' — ')
        for i in range(len(result)):
            if result[i] == word.lower():
                print('Синоним:', result[(i+1) % len(result)].title())
                flag = False
                break
    if flag:
        print('Такого слова в словаре нет')
