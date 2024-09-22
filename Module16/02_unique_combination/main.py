# TODO здесь писать код
def my_list():
    my_list = []
    number = int(input('Введите количество элементов в списке: '))
    for i in range(number):
        num = int(input(f'Введите значение {i+1} элемента списка: '))
        my_list.append(num)
    return my_list

def merge_sorted_lists(list1, list2):
    list1.extend(list2)
    for elem in range(len(list1)):
        for i in range(elem + 1, len(list1)):
            if list1[elem] > list1[i]:
                list1[elem], list1[i] = list1[i], list1[elem]
    for elem in list1:
        counter = list1.count(elem)
        for i in range(counter - 1):
            list1.remove(elem)
    return list1

list1 = my_list()
list2 = my_list()

print(list1)

print(list2)

merged = merge_sorted_lists(list1, list2)
print('Отсортированный список:', merged)


# Пример использования:
# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 5, 6, 8, 10]
# merged = merge_sorted_lists(list1, list2)
# print(merged)