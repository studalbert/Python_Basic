# TODO здесь писать код

def summ_num(number):
    summ = 0
    while number:
        summ = number % 10
        number //= 10
    return summ

def count_num(number):
    count = 0
    while number:
        number //= 10
        count += 1
    return count

number = int(input('Введите число '))
summ = summ_num(number)
count = count_num(number)
print(f'Сумма чисел {summ}')
print(f'Количество цифр в числе: {count}')
print(f'Разность суммы и количества цифр: {summ - count}')