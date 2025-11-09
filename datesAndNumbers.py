import math
import random
import datetime


#absolute value
num1=-99
print(num1)
print(abs(num1))



#rounding
num2=34.789
print(num2)
print(round(num2))
print(round(num2 ,2))
print(round(num2 ,1))
print(round(num2 ,0))

#power
print(pow(num2,2))
print(round(pow(num2,2)))

#max and min
numbers=[22,23,49,45,23,89,99]
print(max(numbers))
print(min(numbers))

#sum
print(sum(numbers))

#sqrt
print(math.sqrt(numbers[2]))

#remainder
print(math.remainder(numbers[3],2))

#return random numbers
print(random.randint( num1,int(num2)))

#date and time
date=datetime.date(2020,12,30)
print(date)
print(date.day)
print(date.month)
print(date.year)
print(datetime.date.today())
print(datetime.date.today().strftime("%A %B %Y"))


time=datetime.time(13,30,23)
print(time)
print(time.hour)
print(time.minute)
print(time.second)
print(datetime.date.today())



