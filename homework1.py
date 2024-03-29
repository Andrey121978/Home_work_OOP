class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average_grade = 0
        average_grade_list = []
        for grade in self.grades.values():
            for i in grade:
                average_grade_list.append(i)
        average_grade = sum(average_grade_list) / len(average_grade_list)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade:.1f}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы:{', '.join(self.finished_courses)}"
#Дописать принт
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
    def __str__(self):
        average_grade = 0
        average_grade_list = []
        for grade in self.grades.values():
            for i in grade:
                average_grade_list.append(i)
        average_grade = sum(average_grade_list) / len(average_grade_list)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}"
class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']

some_lecturer = Lecturer('Sam', 'Brown')
some_lecturer.courses_attached += ['Git', 'Python']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 9)
some_student.rate_hw(some_lecturer, 'Git', 10)
some_student.rate_hw(some_lecturer, 'Python', 9)


print(some_student)
print(some_reviewer)
print(some_lecturer)
