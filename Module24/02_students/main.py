# TODO здесь писать код
class Student:
    def __init__(self, surname_name, group_num, grade):
        self.surname_name = surname_name
        self.group_num = group_num
        self.grade = grade

    def average_mark(self):
        average_mark = sum(self.grade) / len(self.grade)
        return average_mark

    def print_info(self):
        print(f'Фамилия Имя: {self.surname_name}\nНомер группы: {self.group_num}\nСредний балл: {self.average_mark()}\n')



student_1 = Student('Попов Вова', 7, [4,5,3,3,5])
student_2 = Student('Иванов Иван', 7, [3,4,4,3,4])
student_3 = Student('Сидоров Вова', 7, [4,4,3,4,5])
student_4 = Student('Попов Иван', 7, [3,4,5,3,3])
student_5 = Student('Ленова Лена', 7, [5,5,3,3,5])
student_6 = Student('Васильев Вася', 7, [5,4,5,5,4])
student_7 = Student('Васильев Вова', 7, [4,4,4,4,4])
student_8 = Student('Жуков Иван', 7, [3,3,5,3,3])
student_9 = Student('Капустин Женя', 7, [2,2,3,3,2])
student_10 = Student('Помидоров Саша', 7, [5,5,5,5,5])
students_lst = [student_1, student_2, student_3, student_4, student_5, student_6, student_7, student_8, student_9, student_10]
for i in range(len(students_lst)):
    for j in range(i+1, len(students_lst)):
        if students_lst[i].average_mark() > students_lst[j].average_mark():
            students_lst[i], students_lst[j] = students_lst[j], students_lst[i]

for elem in students_lst:
    elem.print_info()


