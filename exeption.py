try:
    num1 = int(input('Enter number 1 : '))
    num2 = int(input('Enter number 2 : '))
    print('the result = ', num1 / num2)
except:
    print('Error!!')

else:
    print('no error')

finally:
    print('the end ')




myList = [1, 2, 0]

try:
    print("the result = ", myList[1] / myList[2])
except ZeroDivisionError:
    print("ZeroDivisionError!!")
except IndexError:
    print("IndexError!!")

#assert
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    evenNumber = num / 2
    print(evenNumber)

#relase
age = int(input("Enter your age:"))

if age < 18:
    raise Exception("Sorry, This game for more than 18 age ")

print("Start game")


