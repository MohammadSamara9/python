class Employee:
    def __init__(self,name):
        self.name=name
        self._tel='+970238798656'
        self.__salary=10000


    def get_salaray(self):
        return self.__salary




emp1=Employee('John')
emp2=Employee('Jane')

print(emp1.name,emp2.name)
print(emp1._tel,emp2._tel)
print(emp1.get_salaray(),emp2.get_salaray())



class Teacher:
    def __init__(self,name):
        self.name=name
        self._tel='+970238798656'
        self.__salary=10000

    def _job(self):
        print("teacher job")

    def __give_raise(self):
        self.__salary=self.__salary+500
        print("your salary is",self.__salary)


    def get_raise(self):
        self.__give_raise()





th1=Teacher('John')
th2=Teacher('Jane')

th1._job()
th2._job()

th2.get_raise()

