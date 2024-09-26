students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def result(my_dict):
    student_interests = []
    summ_family = 0
    pairs = []
    for key, value in my_dict.items():
        pairs.append((key, value['age']))
        student_interests.extend(value['interests'])
        summ_family += len(value['surname'])

    return student_interests, summ_family, pairs

student_interests, summ_family, pairs = result(students)
print('Список пар "ID студента — возраст":', pairs)
print('Полный список интересов всех студентов:', set(student_interests))
print('Общая длина всех фамилий студентов:', summ_family)
# TODO исправить код
