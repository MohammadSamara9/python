class Student:
    def print_info(self):
        print('This is the code for class Student')

class Teacher:
    def print_info(self):
        print('This is the code for class Teacher')

student1 = Student()
teacher1 = Teacher()

student1.print_info()
teacher1.print_info()







class Circle:
    def draw(self):
        print('The code for drawing the circle')

class Square:
    def draw(self):
        print('The code for drawing the square')

class Triangle:
    def draw(self):
        print('The code for drawing the triangle')

circle1 = Circle()
square1 = Square()
triangle1 = Triangle()

shapes = [circle1, square1, triangle1]

for shape in shapes:
    shape.draw()



class Student:
    def print_info(self):
        print('This is the code for class Student')

class Teacherr:
    def print_info(self):
        print('This is the code for class Teacher')

student = Student()
teacher = Teacherr()

def func(obj):
    obj.print_info()


func(student)
func(teacher)
