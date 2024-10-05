# TODO здесь писать код
import random
class House:
    def __init__(self, food = 50, money = 0):
        self.food = food
        self.money = money

class Human:
    def __init__(self, name, house, degree_satiety = 50):
        self.name = name
        self.degree_satiety = degree_satiety
        self.house = house

    def to_eat(self):
        self.degree_satiety += 5
        house.food -= 5

    def shopping(self):
        house.food += 10
        house.money -= 5

    def work(self):
        self.degree_satiety -= 5
        house.money += 10

    def play(self):
        self.degree_satiety -= 5

    def live_one_day(self, person):
        lst = list(range(1,7))
        cub = random.choice(lst)
        if person.degree_satiety < 20:
            person.to_eat()
            print(f'Поели. Сытость +5, еда -5')
        elif house.food < 10:
            person.shopping()
            print(f'Сходили в магазин. деньги -5, еда +10')
        elif house.money < 50:
            person.work()
            print(f'Поработали. Сытость -5, деньги +10')
        elif cub == 1:
            person.work()
            print(f'Поработали. Сытость -5, деньги +10')
        elif cub == 2:
            person.to_eat()
            print(f'Поели. Сытость +5, еда -5')
        else:
            person.play()
            print(f'Поиграли. Сытость -5')



house = House()
human = Human('Саша', house)
human2 = Human('Женя', house)
for i in range(365):
    print(f'\n{i+1} день. Сытость : {human.degree_satiety} и {human2.degree_satiety}, Деньги : {house.money}, Еда : {house.food}')
    human.live_one_day(human)
    human2.live_one_day(human2)
    if human.degree_satiety < 0 or human2.degree_satiety < 0:
        print(f'Человек умер спустя {i+1} дней')
        break

