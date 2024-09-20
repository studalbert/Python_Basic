# TODO здесь писать код
numbers = int(input('Элементов в списке: '))
old_list = []
for i in range(numbers):
    num = int(input('Введите число: '))
    old_list.append(num)
print('Изначальный список:', old_list)
shift = int(input('Сдвиг: '))
new_list = []
for _ in range(len(old_list)):
    new_list.append(old_list[(_ - shift) % len(old_list)])
    # new_list.append(old_list[(len(old_list) - i - shift) % len(old_list)])

print('Сдвинутый список:', new_list)




