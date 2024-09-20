# TODO здесь писать код

# Список чисел для работы (итоговый алгоритм проверьте на разных списках, придуманных самостоятельно):
numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
print('Начальный список:', numbers_list)
#1
print('Отсортированный список:', end = ' ')
for i in range(-1, -len(numbers_list)-1, -1):
    if numbers_list[i] % 2 == 0:
        print(numbers_list[i], end = ' ')
#2
print()
print('Отсортированный список:', end = ' ')
for i in range(len(numbers_list)):
    if numbers_list[len(numbers_list) - i - 1] % 2 == 0:
        print(numbers_list[len(numbers_list) - i - 1], end = ' ')