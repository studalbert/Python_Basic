# TODO здесь писать код
#1 способ
from collections.abc import Iterator


class NumsSquares:
   def __init__(self, number:int) -> None:
       self.__number = number
       self.__count = 0

   def __iter__(self) -> Iterator[int]:
       self.__count = 0
       return self

   def __next__(self) -> int:
       self.__count += 1
       if self.__count > self.__number:
           raise StopIteration
       num = self.__count**2
       return num
#2 способ
def nums_squares(number:int) -> Iterator[int]:
    count = 0
    while count < number:
        count += 1
        yield count**2

#3 способ
number = 7
nums_squares_gen = (num**2 for num in range(1, number+1))
for elem in NumsSquares(7):
    print(elem, end = ' ')
print()
for elem in nums_squares(7):
    print(elem, end=' ')
print()
for elem in nums_squares_gen:
    print(elem, end = ' ')





