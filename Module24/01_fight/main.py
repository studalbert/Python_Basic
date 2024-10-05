# TODO здесь писать код
import random
class Warrior:
    def __init__(self, health = 100, name = 'Воин'):
        self.health = health
        self.name = name

    def damage(self):
        self.health -= 20
        print(f'У {self.name} осталось {self.health} очков здоровья')
        if self.health == 0:
            print(f'У {self.name} не осталось очков здоровья. Воин погиб')
            return False
        else:
            return True

warrior_1 = Warrior(name = 'Воин 1')
warrior_2 = Warrior(name = 'Воин 2')
flag = True
while flag:
    who_hit = random.choice([1, 2])
    if who_hit == 1:
        print('\nПервый воин атакует второго')
        flag = warrior_2.damage()
        if flag == False:
            print('Победу одержал первый воин')
    if who_hit == 2:
        print('\nВторой воин атакует первого')
        flag = warrior_1.damage()
        if flag == False:
            print('Победу одержал второй воин')

