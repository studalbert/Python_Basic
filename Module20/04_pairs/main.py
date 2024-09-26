# TODO здесь писать код
from random import randint

origin_list = [randint(0,10) for i in range(10)]
print(origin_list)
new_list = [(origin_list[i], origin_list[i+1]) for i in range(0,len(origin_list), 2)]
print(new_list)