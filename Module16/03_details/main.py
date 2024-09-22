shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

# TODO здесь писать код

while True:
        detail = input('Название детали: ')
        counter = 0
        summ = 0
        for elem in range(len(shop)):
                if shop[elem][0] == detail:
                        counter += 1
                        summ += shop[elem][1]
        print('Количество деталей — ', counter)
        print('Общая стоимость — ', summ)