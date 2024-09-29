# TODO здесь писать код
def pnt_num(num):
    if num == 1:

        return print(num)
    pnt_num(num - 1)
    print(num)
num = int(input('Введите num: '))
pnt_num(num)