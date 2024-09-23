# TODO здесь писать код
size_skates = []
size_foot = []
skates = int(input('Количество коньков: '))
for i in range(skates):
    size = int(input(f'Размер {i+1} пары: '))
    size_skates.append(size)
people = int(input('Количество людей '))
for i in range(people):
    size = int(input(f'Размер ноги {i+1} человека: '))
    size_foot.append(size)

counter = 0
for foot in size_foot:
    for skate in size_skates:
        if foot == skate:
            counter += 1
            size_skates.remove(skate)
            break
print('Наибольшее кол-во людей, которые могут взять ролики', counter)