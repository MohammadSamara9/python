class Vehicle:
    def __init__(self, company, model, year,price):
        self.company = company
        self.model = model
        self.year = year
        self.price = price


def move(self):
    print("Moving")


def stop(self):
    print("Stopping")



    def display(self):
        print("Vehicle type not specified")


class Car(Vehicle):
    #overriding
    def display(self):
        print(f"Company: {self.company}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")



car1=Car("BMW", "BMW", "2009", 100)

print(car1.company)
print(car1.model)
print(car1.year)
car1.display()



class Polygon:
    def p_display(self):
        print("This is Polygon class")

class Shape:
    def sh_display(self):
        print("This is Shape class")

class Square(Polygon, Shape):
    def sq_display(self):
        print("This is Square class")

sq = Square()
sq.sq_display()
sq.sh_display()


#MRO
class A:
    def do_this(self):
        print('Doing this in class A')

class B(A):
    pass

class C:
    def do_this(self):
        print('Doing this in class C')

class D(B, C):
    pass

obj = D()
obj.do_this()
print(D.mro())


#وراثة Constructor
class Person:
    def __init__(self, first_name, surname, tel):
        self.first_name = first_name
        self.surname = surname
        self.tel = tel

    def full_name(self):
        return self.first_name + " " + self.surname

class Employee(Person):
    def __init__(self, first_name, surname, tel, salary):
        super().__init__(first_name, surname, tel)
        self.salary = salary

    def give_raise(self, amount):
        self.salary = self.salary + amount

employee1 = Employee("John", "Smith", "1999", 20000)