# TODO здесь писать код
class Child:
    def __init__(self, name, age, calmness = False, hunger = True):
        self.name = name
        self.age = age
        self.calmness = calmness
        self.hunger = hunger

    def print_child(self):
        print(f'\nИмя: {self.name}\nВозраст: {self.age}')



class Parent:
    def __init__(self, name, age, child_lst):
        self.name = name
        self.age = age
        self.child_lst = child_lst

    def print_info(self):
        print(f'Имя родителя: {self.name}\nВозраст: {self.age}\n')
        print('Дети:')
        for child in self.child_lst:
            child.print_child()

    def calmness_child(self):
        for child in self.child_lst:
            child.calmness = True

    def to_feed_child(self):
        for child in self.child_lst:
            child.hunger = False


def correct_age_child(age_parent):
    age_child = int(input('Введите возраст ребенка: '))
    if age_child + 16 > age_parent:
        print('Должен быть меньше возраста родителя хотя бы на 16 лет')
        correct_age_child(age_parent)
    else:
        return age_child

for i in range(1):
    name_parent = input('Введите имя родителя: ')
    age_parent = int(input('Введите возраст родителя: '))

for i in range(1):
    name_child = input('Введите имя ребенка: ')
    age_child = correct_age_child(age_parent)

child = Child(name_child, age_child)
parent = Parent(name_parent, age_parent, [child])
parent.print_info()