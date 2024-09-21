# TODO здесь писать код
numbers = int(input('Элементов в списке: '))
my_list = []
for i in range(numbers):
    num = int(input('Введите число: '))
    my_list.append(num)
print('Изначальный список:', my_list)
for i in range(numbers):
    for j in range(i+1, numbers):
        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]
print('Отсортированный список:', my_list)