# TODO здесь писать код
import re

numbers = ['9999999999', '999999-999', '99999x9999']
pattern = re.compile(r'^[89]\d{9}$')
for i in range(len(numbers)):
    if pattern.search(numbers[i]):
        print(f'{i+1} номер: все в порядке')
    else:
        print(f'{i+1} номер: не подходит')
