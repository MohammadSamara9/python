class Student:
    university_name='birzeit university'
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def talk(self):
        print(f"hi my name is {self.name} and i have {self.age} years old")



std1=Student("mohammed",22,95)
std2=Student("ali",20,75)
std3=Student("john",19,90)
print(std1.name)
print(std1.age)
print(std1.marks)
std1.talk()

#dir
print(dir(std1))

#add attributes
std2.v_hours=15
print(dir(std1))
print(dir(std2))

#delete attributes
del std2.v_hours
print(dir(std2))

#delete object
del std2

#stsic member
print(std1.university_name)
print(std3.university_name)


#setter and getter
class Myclass:
    def set_value(self,value):
        self.value=value

    def get_value(self):
        return self.value


ob1=Myclass()
ob2=Myclass()

ob1.set_value(1)
ob2.set_value(2)

print(ob1.get_value())
print(ob2.get_value())
print(ob1.value)

####
class Myint:
    def set_value(self,val):
        if(type(val)==int):
            self.val = val
        else:
            print("the value is not integer")

    def get_Value(self):
        return self.val


    def increment(self):
        self.val+=1



a=Myint()
b=Myint()

a.set_value(34)
b.set_value(21)

print(a.get_Value())
print(b.get_Value())


a.increment()
print(a.get_Value())
b.increment()
print(b.get_Value())
