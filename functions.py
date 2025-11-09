
def greet():
    name=input("enter your name: ")
    age=input("enter your age: ")
    print(f"Hello {name} and your age is {age}")
    print("hello " +name+ " your age is: " +age)


def print_numbers(x):
    for i in range(1,x):
        print(i)

def sum(n1,n2):
    print(n1+n2)
    return n1+n2

def subtraction(n1,n2):
    return n1-n2




greet()
print_numbers(5)
print_numbers(8)
print_numbers(7)
sum(2,3)
sum("hello"," world")
res=subtraction(9,3)
print(res)
value=sum(9,7) -subtraction(4,2)
print(value)
print_numbers(sum(2,4))







