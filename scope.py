#global scope
name2="mohammed"


#local scope
def func():

    name = "Ali"
    global name3
    name3="mosa"
    print(name)
    print(name2)

func()
name = "Ahmad"
print(name)
print(name3)



