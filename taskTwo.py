def check(number):
    if number==0:
        print("error")
    elif number%2==0:
        print("number is even")
    else:
        print("number is odd")


numbers=input("enter the numbers with space: ").split()
for n in numbers:
    numbers.append(int(n))