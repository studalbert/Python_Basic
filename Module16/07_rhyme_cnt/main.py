people = int(input('Кол-во человек: '))
people_list = list(range(1, people +1))
num = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {num}-й человек ')
index = 0
while len(people_list) != 1:
    print('Текущий круг людей:', people_list)
    print('Начало счета с номера', people_list[abs(index) % len(people_list)])

    del_people = people_list[(index + num) % len(people_list)-1]
    index = people_list.index(del_people)

    print('Выбывает человек под номером', del_people)
    people_list.remove(del_people)

    #num % len(people_list) начинают считать с этого индекса
    #people_list[num%people_list-1] выбывает этот индекс

print('\nОстался человек под номером', people_list[0])
