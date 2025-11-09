from operator import truediv
from xml.dom.minidom import ProcessingInstruction

name = 'Khalid'
age = 18
is_student = True
student_mark=69.72



print(type(name))
print(type(age))
print(type(is_student))


name2,age2,gender,drivinglicense='mohammed',30,'male',None
drivinglicense=input("do you have driving license")
print(f"your name {name2} and your age is {age2} and your gender is {gender} and did you have driving license?? {drivinglicense}")



floatAge=float(age)
print(float(age))

in_mark=int(student_mark)
print(in_mark)

str_mark=str(student_mark)
print(str_mark)
print(type(str_mark))


informations=['ali','samer','mohammed',23,23,45,False,True,True]
print(informations)
print(type(informations))
print(informations[0])
informations[2]="ibrahim"
print(informations[2])
informations.append("moe")
print(informations)
informations.remove("moe")
informations.insert(2,"moe")
print(informations)
informations.clear()
print(informations)


student_one=("amal","female",16)
print(student_one[0])
print(type(student_one))



child={
  'name':"noor",
  'age':12,
  'gender':'female',
}

print(type(child))
print(child.values())
print(child.keys())
print(child)
print(child.items())
print(child['name'])
