from datetime import datetime


def info(names,ages,days):
    number = len(ages)
    for i in range (len (names)):
        print(f"{i} is {ages[i]} years old and she/he was born in {days[i]}")

    if number>1:
        old = max(ages)
        young = min(ages)
        index_max_name = ages.index(old)
        index_min_name = ages.index(young)
        print(f"the oldest one is {names[index_max_name]}")
        print(f"the youngest one is {names[index_min_name]}")

    print(f"total people: {number}")







print("__________________WELCOME_____________________")
x=True
list_name=[]
list_ages=[]
list_days=[]

today=datetime.today()

while x:
    name, date = input("enter the name the birth date:").split()

    list_name.append(name)

    date_ = datetime.strptime(date, "%d-%m-%Y")
    if date_ > today :
        print(f"Invalid date-{name}")
        list_name.remove(name)
        continue

    age = today.year - date_.year

    list_ages.append(age)

    date_str = date_.strftime(" %A")

    list_days.append(date_str)


    x=bool(int(input("you want to enter more names:")) )




info(list_name,list_ages,list_days)
























