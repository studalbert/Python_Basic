# TODO здесь писать код
from collections.abc import Iterator


class Node:

    def __init__(self, num:int) -> None:
        self.num = num
        self.next = None

    def __str__(self) -> str:
        return str(self.num)

class LinkedList:

    def __init__(self) -> None:
        self.number = None
        self.count = 0

    def append(self, number:int) -> None:
        new_num = Node(number)
        if not self.number:
            self.number = new_num
            return
        next_number = self.number
        while next_number.next:
            next_number = next_number.next
        next_number.next = new_num

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        self.count += 1
        if self.count == 1:
            return self.number
        else:
            self.number = self.number.next
            if not self.number:
                raise StopIteration
            return self.number

    def get(self, index:int) -> int:
        count = 0
        number = self.number
        while count != index:
            count += 1
            number = number.next
        return int(str(number))

    def remove(self, index:int) -> None:
        count = 0
        number = self.number
        if index == 0:
            self.number = self.number.next
        else:
            while count != index - 1:
                count += 1
                number = number.next
            number.next = number.next.next

    def __str__(self) -> str:
        res = [int(str(self.number))]
        number = self.number.next
        while number:
            res.append(int(str(number)))
            number = number.next
        return str(res)



my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
my_list.append(40)
my_list.append(50)
print(my_list)
for elem in my_list:
    print(elem)
