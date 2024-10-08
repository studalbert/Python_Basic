# TODO здесь писать код
class Stack:
    def __init__(self):
        self.lst = []

    def add(self, str):
        self.lst.append(str)
    def pop(self, str):
        self.lst.remove(str)
    def __str__(self):
        return ', '.join(self.lst)

class TaskManager:
    def __init__(self):
        self.dct = {}
    def new_task(self, str, int):
        if not self.dct.get(int):
            stek = Stack()
            stek.add(str)
            self.dct[int] = stek
        else:
            if not str in self.dct[int].lst:
                self.dct[int].add(str)

    def del_task(self, str, int):
        self.dct[int].pop(str)

    def info(self):

        for key, value in sorted(self.dct.items()):
            print(f'{key} : {value}')

    def __str__(self):
        res_lst = []
        for key, value in sorted(self.dct.items()):
            res_lst.append(f'{key} : {value}')
        return '\n'.join(res_lst)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
manager.del_task('сделать уборку', 4)
print(manager)
