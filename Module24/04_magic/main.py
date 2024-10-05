# TODO здесь писать код
class Water:
    def __add__(self, other):
        if isinstance(other, Fire):
            return 'Пар'
        elif isinstance(other, Air):
            return 'Шторм'
        elif isinstance(other, Earth):
            return 'Грязь'

class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return 'Пар'
        elif isinstance(other, Air):
            return 'Молния'
        elif isinstance(other, Earth):
            return 'Лава'

class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return 'Молния'
        elif isinstance(other, Water):
            return 'Шторм'
        elif isinstance(other, Earth):
            return 'Пыль'
class Earth:
    def __add__(self, other):
        if isinstance(other, Fire):
            return 'Лава'
        elif isinstance(other, Air):
            return 'Пыль'
        elif isinstance(other, Water):
            return 'Грязь'


print('Выберите два элемента из предложенных: Вода, огонь, воздух, земля.')
try:
    elem_1 = input('Первый элемент: ')
    elem_2 = input('Второй элемент: ')
    if elem_1.lower() in ['вода', 'огонь', 'воздух', 'земля'] and elem_2.lower() in ['вода', 'огонь', 'воздух', 'земля']:
        if elem_1.lower() == 'вода':
            elem_1 = Water()
        elif elem_1.lower() == 'огонь':
            elem_1 = Fire()
        elif elem_1.lower() == 'воздух':
            elem_1 = Air()
        elif elem_1.lower() == 'земля':
            elem_1 = Earth()

        if elem_2.lower() == 'вода':
            elem_2 = Water()
        elif elem_2.lower() == 'огонь':
            elem_2 = Fire()
        elif elem_2.lower() == 'воздух':
            elem_2 = Air()
        elif elem_2.lower() == 'земля':
            elem_2 = Earth()
    else:
        raise SyntaxError

except SyntaxError:
    print('Нужно написать один из четырех элементов')

else:
    print('Получится:', (elem_1 + elem_2))