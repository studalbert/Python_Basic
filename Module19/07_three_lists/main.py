# TODO здесь писать код
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
result2 = []
def task_1(array_1, array_2, array_3):
    result1 = []
    for num in array_1:
        if num in array_2 and num in array_3:
            result1.append(num)
    return result1

print('Задача 1')
print('Решение без множеств:', task_1(array_1, array_2, array_3))
print('Решение с множествами:', set(array_1) & set(array_2) & set(array_3))

def task_2(array_1, array_2, array_3):
    result2 = []
    for num in array_1:
        if num not in array_2 and num not in array_3:
            result2.append(num)
    return result2

print('Задача 2')
print('Решение без множеств:', task_2(array_1, array_2, array_3))
print('Решение с множествами:', set(array_1) - set(array_2) - set(array_3))