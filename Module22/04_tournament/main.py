# TODO здесь писать код
from os.path import split

first_tour = open('first_tour.txt', 'r')
first_tour_lst = first_tour.read().split('\n')
first_tour.close()
point = first_tour_lst[0]
first_tour_lst.remove(point)

second_tour = open('second_tour.txt', 'w')

def second_tour_result_lst(lst):
    result = []
    for person in lst:
        person = person.split()
        person_point = int(person[2])
        if person_point > int(point):
            result.append(f'{person[1][0]}. {person[0]} {person[2]}')
    return result

second_tour_lst = second_tour_result_lst(first_tour_lst)

def sort_lst(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if int(lst[i][-2:]) < int(lst[j][-2:]):
                lst[i], lst[j] = lst[j], lst[i]


sort_lst(second_tour_lst)
count_people = len(second_tour_lst)
second_tour.write(f'{str(count_people)}\n')
num = 1
for elem in second_tour_lst:
    second_tour.write(f'{num}) {elem}\n')
second_tour.close()