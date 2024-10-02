# TODO здесь писать код
import random
lst = list(range(13))
summ = 0
while summ < 777:
    try:
        num = int(input('Введите число: '))
        summ += num
        if random.choice(lst) == 0:
            raise BaseException('Вас постигла неудача!')
        with open('out_file.txt', 'a') as out_file:
            out_file.write(f'{str(num)}\n')

    except ValueError:
        print('Ошибка. Пожалуйста, введите корректное число.')

print('Вы успешно выполнили условие для выхода из порочного цикла!')