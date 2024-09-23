# TODO здесь писать код
numbers = int(input('Количество чисел: '))
my_list = []
for i in range(numbers):
    num = int(input('Число: '))
    my_list.append(num)
print('Последовательность:', my_list)
new_list = []
def simm(my_list):
    counter = 0
    for i in range(len(my_list)//2):
        if my_list[i] == my_list[len(my_list) - 1 - i]:
            counter += 1
    if len(my_list) // 2 == counter:
        return False #Симметричный
    else:
        return True
counter = 0
while simm(my_list):
    new_list.append(my_list[0])
    my_list.remove(my_list[0])
    counter += 1
print('Нужно приписать чисел:', counter)
print('Сами числа:', new_list)
new_list = new_list + my_list + new_list
print('Результат:', new_list)
