# TODO здесь писать код
num_order = int(input('Введите количество заказов: '))
orders = dict()
for i in range(num_order):
    order = input(f'{i+1} заказ: ')
    result = order.split()
    if result[0] not in orders:
        orders[result[0]] = {result[1] : result[2]}
    else:
        if result[1] not in orders[result[0]]:
            orders[result[0]][result[1]] = result[2]
        else:
            orders[result[0]][result[1]] = int(orders[result[0]][result[1]]) + int(result[2])

for family in orders:
    print(f'{family}:')
    for pizza in orders[family].keys():
        print(f'         {pizza}: {orders[family][pizza]}')