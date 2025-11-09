def guessNumber(number,true_Number):
    if number==true_Number:
        print("correct number")
        return False
    elif number<true_Number:
        print("greater than number")
        return True
    elif number>true_Number:
        print(" less than number")
        return True



trueNumber= int (input("enter the true number: "))
num= int (input("enter the number: "))
x=guessNumber(num,trueNumber)

while x:
    num= int (input("enter the number: "))
    x=guessNumber(num,trueNumber)

