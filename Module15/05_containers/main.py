# TODO здесь писать код
num = int(input('Количество контейнеров: '))
count = 0
boxes = []
while count != num:
    weight = int(input('Введите вес контейнера: '))
    if weight > 200:
        print('Вес не должен превышать 200кг')
    else:
        boxes.append(weight)
        count += 1

new_weight = int(input('Введите вес нового контейнера: '))
for index, box in enumerate(boxes):
    if new_weight > box:
        print('Номер, который получит новый контейнер:', index + 1)
        break


