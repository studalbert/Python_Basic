nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

# TODO здесь писать код
def result_last(lst):
    result_list = []

    def result(lst):
        if isinstance(lst, int):
            result_list.append(lst)
        else:
            for value in lst:
                result(value)
    result(lst)
    return result_list
print('Ответ:', result_last(nice_list))