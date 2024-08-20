class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_info(self):
        return self.name, self.age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, name: str, age: int, grade: int, subjects: list):
        Person.__init__(self, name, age)
        self.__grade = grade
        self.subjects = subjects

    def get_info(self):
        return f"Имя:{self.name}, Возраст:{self.age}, Класс:{self.__grade}, Изучаемые предметы:{self.subjects}"

    def get_grade(self):
        return self.__grade

    def finish_grade(self):
        self.__grade = self.__grade + 1
        return self.__grade


class Worker:
    def __init__(self, position: str, wage: int):
        self.position = position
        self.wage = wage

    def get_position(self):
        return self.position

    def get_wage(self):
        return self.wage


class Teacher(Worker, Person):
    def __init__(self, name: str, age: int, position: str, wage: int):
        Worker.__init__(self, position, wage)
        Person.__init__(self, name, age)

    def get_info(self):
        return f"Имя:{self.name}, Возраст:{self.age}, Должность:{self.position}, Зарплата:{self.wage}"


class Group:
    def __init__(self, group_name: str, students: list[Student], teacher: Teacher):
        self.group_name = group_name
        self.students = students
        self.teacher = teacher

    def group_info(self):
        for student in self.students:
            print(student.get_info())
        print(f"Группа: {self.group_name}, Куратор: {self.teacher.get_info()} Количество студентов:{len(self.students)}")

    def students_number(self):
        print(len(self.students))


"""
stud = Student("Иванов Василий Викторович",11,3,["maths","physics"])
print(stud.get_info())

stud.finish_grade()
print(f"Перевели Васю в следующий класс: {stud.get_grade()}")

teach = Teacher("Ярцев Валерий Рустэмович",20,"Informatics teacher",200)
print(teach.get_info())
"""

student1 = Student("Виталий", 23, 3, ["Maths", "Physcis"])
student2 = Student("Геннадий", 21, 3, ["Maths", "Physcis"])
student3 = Student("Иван", 43, 3, ["Maths", "Physcis", "PE"])
teacher = Teacher("Ярцев Валерий Рустэмович", 20, "Informatics teacher", 200)
group = Group("3A", [student1, student2, student3], teacher)
group.group_info()
