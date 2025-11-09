
#2D list
value=[
    [1,2,3],
    [9,7,4],
    [9,4,5]
]
print(value[0][2])
print(value[2][2])
print(value[1][0])
print(value[1])

#filter
ages=[34,23,12,11,34,56,34]
def filtered_ages(age):
    return age>=18

print(list(filter(filtered_ages,ages)))

#map
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def aquare(number):
    return number**2

print(list(map(aquare,numbers)))

#sort
list_one=[100,23,12,2]
list_two=['mohammed','ahmad','samer','morad']
list_one.sort()
list_two.sort()
print(list_one)
print(list_two)

list_one.sort(reverse=True)
list_two.sort(reverse=True)
print(list_one)
print(list_two)

#reverse
list_two.reverse()
print(list_two)

#list comprehension
multiplied_list=[num*2 for num in list_one if num>10 and num%2==0]
print(multiplied_list)