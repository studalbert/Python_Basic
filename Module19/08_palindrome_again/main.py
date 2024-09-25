# TODO здесь писать код
text = input('Введите строку: ')
text = list(text)
text_set = set(text)

def palindrome(text, text_set):
    counter = 0
    flag = True
    for sym in text_set:
        if text.count(sym) % 2 == 1:
            counter += 1
        if counter > 1:
            flag = False
            print('Нельзя сделать палиндромом')
            break
    if flag:
        print('Можно сделать палиндромом')

palindrome(text, text_set)
