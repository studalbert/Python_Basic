# TODO здесь писать код
from typing import List
from functools import reduce

if __name__ == '__main__':
    floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
    names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
    numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

    #Каждое число из списка floats возводится в третью степень и округляется до трёх знаков после запятой.
    res_1: List[float] = list(map(lambda x: round(x**3, 3), floats))

    #Из списка names берутся только те имена, в которых есть минимум пять букв.
    res_2: List[str] = list(filter(lambda x: len(x) >= 5, names))

    # Из списка numbers берётся произведение всех чисел.
    res_3: int = reduce(lambda x, y: x * y, numbers)

    print(f'{res_1}\n{res_2}\n{res_3}')


