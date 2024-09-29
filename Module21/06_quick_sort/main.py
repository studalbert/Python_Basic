# TODO здесь писать код

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    last_elem = lst[-1]
    res1 = [x for x in lst if x < last_elem]
    res2 = [x for x in lst if x == last_elem]
    res3 = [x for x in lst if x > last_elem]

    res1_sort = quick_sort(res1)
    res3_sort = quick_sort(res3)

    return res1_sort + res2 + res3_sort

print(quick_sort([5, 8, 9, 4, 2, 9, 1, 8]))

