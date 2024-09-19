# TODO здесь писать код
num = int(input('Введите число: '))
for i in range(2, num+1):
    if num % i == 0:
        print(f'Наименьший делитель, отличный от единицы: {i}')
        break