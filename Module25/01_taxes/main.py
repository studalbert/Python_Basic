# TODO здесь писать код
class Property:
    def __init__(self, worth):
        self.__worth = worth

    def get_worth(self):
        return self.__worth

    def set_worth(self, worth):
        self.__worth = worth

    def tax(self):
        pass

class Apartment(Property):
    def tax(self):
        tax = self.get_worth() / 1000
        return tax

class Car(Property):
    def tax(self):
        tax = self.get_worth() / 200
        return tax

class CountryHouse(Property):
    def tax(self):
        tax = self.get_worth() / 500
        return tax


money = int(input('Введите количество денег: '))
worth = int(input('Введите стоимость имущества: '))
car = Car(worth)
print('Налог на имущество:', car.tax())
if car.tax() > money:
    print(f'Не хватает {car.tax() - money} рублей')
else:
    print(f'После выплаты налога останется: {money - car.tax()} рублей')