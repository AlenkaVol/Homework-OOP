class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _get_average_grade(self):
        total = 0
        counter = 0
        for value in self.grades.values():
            for grade in value:
                total += grade
                counter += 1
        average_grade = round(total / counter, 1)
        return average_grade

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: ' \
              f'{self._get_average_grade()} \nКурсы в процессе изучения: {",".join(self.courses_in_progress)} \n' \
              f'Завершенные курсы: {",".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Неправильное сравнение. Можно сравнивать между собой либо только студентов, либо только лекторов')
            return
        return self._get_average_grade() < other._get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _get_average_grade(self):
        total = 0
        counter = 0
        for value in self.grades.values():
            for grade in value:
                total += grade
                counter += 1
        average_grade = round(total / counter, 1)
        return average_grade

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._get_average_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Неправильное сравнение. Можно сравнивать между собой либо только студентов, либо только лекторов')
            return
        return self._get_average_grade() < other._get_average_grade()


class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


student_1 = Student('Алена', 'Баринова', 'ж')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']
student_2 = Student('Иван', 'Кузнецов', 'м')
student_2.courses_in_progress += ['Git', 'Python']
student_2.finished_courses += ['SQL']

lecturer_1 = Lecturer('Андрей', 'Соловьев')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Елена', 'Брылева')
lecturer_2.courses_attached += ['Git']

reviewer_1 = Reviewer('Дмитрий', 'Киселев')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Александр', 'Жасминов')
reviewer_2.courses_attached += ['Git']

student_1.rate_hw(lecturer_1, 'Python', 9)
student_2.rate_hw(lecturer_1, 'Python', 8)
student_2.rate_hw(lecturer_2, 'Git', 10)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Git', 8)

print(student_1)
print(lecturer_1)
print(reviewer_1)

print(lecturer_1 < lecturer_2)
print(student_1 < student_2)

all_students = []
all_lecturers = []
all_students.append(student_1)
all_students.append(student_2)
all_lecturers.append(lecturer_1)
all_lecturers.append(lecturer_2)

# функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def average_grade_all_students(list_students, course_name):
    total = 0
    counter = 0
    for student in list_students:
        for grade in student.grades.items():
            if course_name in grade:
                total += sum(grade[1])
                counter += len(grade[1])
    average_grade = round(total / counter, 1)
    return average_grade

print(average_grade_all_students(all_students, 'Python'))

# функция для подсчета средней оценки за лекции всех лекторов в рамках конкретного курса
def average_grade_all_lecturers(list_lecturers, course_name):
    total = 0
    counter = 0
    for lecturer in list_lecturers:
        for grade in lecturer.grades.items():
            if course_name in grade:
                total += sum(grade[1])
                counter += len(grade[1])
    average_grade = round(total / counter, 1)
    return average_grade

print(average_grade_all_lecturers(all_lecturers, 'Python'))
