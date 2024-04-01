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

    def get_average_grade(self):
        average_grade_list = []
        for grade in self.grades.values():
            for i in grade:
                average_grade_list.append(i)
        if len(average_grade_list) == 0:
            return 0
        else:
            return sum(average_grade_list) / len(average_grade_list)
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_average_grade():.1f}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

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

    def get_average_grade(self):
        average_grade_list = []
        for grade in self.grades.values():
            for i in grade:
                average_grade_list.append(i)
        if len(average_grade_list) == 0:
            return 0
        else:
            return sum(average_grade_list) / len(average_grade_list)

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_grade():.1f}"
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
def average_grade_course_st(students_list, course):
    sum_grades_count = 0
    sum_grades = 0
    for student in students_list:
        if course in student.grades.keys():
            sum_grades += sum(student.grades[course])
            sum_grades_count += len(student.grades[course])
    return sum_grades / sum_grades_count

def average_grade_course_lec(lecturer_list, course):
    sum_grades_count = 0
    sum_grades = 0
    for lecturer in lecturer_list:
        if course in lecturer.grades.keys():
            sum_grades += sum(lecturer.grades[course])
            sum_grades_count += len(lecturer.grades[course])
    return sum_grades / sum_grades_count

students_list = []
lecturer_list = []
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
next_student = Student('Ben', 'Clark', 'your_gender')
next_student.courses_in_progress += ['Python', 'Java']
next_student.finished_courses += ['Git']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']
next_reviewer = Reviewer('Arnold', 'Ivanov')
next_reviewer.courses_attached += ['Python', 'Java']

some_lecturer = Lecturer('Sam', 'Brown')
some_lecturer.courses_attached += ['Git', 'Python']
next_lecturer = Lecturer('Peter', 'Maverik')
next_lecturer.courses_attached += ['Python', 'Java']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 9)
some_student.rate_hw(some_lecturer, 'Git', 10)
some_student.rate_hw(some_lecturer, 'Python', 9)
some_student.rate_hw(next_lecturer, 'Git', 10)
next_student.rate_hw(some_lecturer, 'Python', 8)
next_reviewer.rate_hw(next_student, 'Java', 9)
next_reviewer.rate_hw(next_student, 'Python', 9)

students_list.append(some_student)
students_list.append(next_student)
lecturer_list.append(some_lecturer)
lecturer_list.append(next_lecturer)

print(some_student)
print(next_student)
print(some_reviewer)
print(next_reviewer)
print(some_lecturer)
print(next_lecturer)

print(next_lecturer < some_lecturer)
print(next_student < some_student)
course = 'Python'
print(f"Средняя оценка за домашние задания Студентов по курсу {course}: {average_grade_course_st(students_list, course)}")
print(f"Средняя оценка за лекции Лекторов по курсу {course}: {average_grade_course_lec(lecturer_list, course)}")
