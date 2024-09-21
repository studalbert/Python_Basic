# TODO здесь писать код
num = int(input('Введите число: '))
numbers = []
for i in range(1, num+1, 2):
    numbers.append(i)
print(f'Список из нечётных чисел от до {num}: {numbers}')
