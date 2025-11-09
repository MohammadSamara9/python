
def info (name,age):
    print(f'hello {name}, you are {age} years old')


#positional arguments
info("mohammed",19)



#keyword arguments
info(age=20,name="sami")
info("ali",age=15)


#defult parameter=optional parameter
def info_1(name="mohammed",age=19,course="Python"):
    print(f'hello {name}, you are {age} years old, course is {course}')

info_1()
info_1("ali")
info_1("ali",22)
info_1("ali",22,"Python")
info_1("Python","ali",22,)

#argument packing
def avg(*args):
    total=sum(args)
    leng=len(args)

    avg=total/leng
    print(avg)


avg(2,5,7,8)

#argument unpacking
informations="ali",22
info(*informations)

#packing and unpacking usage
nums=[3,2,5,2,4,5]
avg(*nums)

#dictionary packing
def info_2(**Kwargs):
    print(Kwargs)
    print(Kwargs.values())
    print(Kwargs.keys())


info_2(name="ali",age=20)
#dictionary unpacking

d={
"names":["mohammed","ali","sami"],
"age":[22,45,21],
"course":"Python"
}
info_2(**d)