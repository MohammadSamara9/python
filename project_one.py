telephone_directory = {
    "0592458777": "amal",
    "0568798656": "ali",
    "0593456789": "noor",
    "056666666": "mohammed",
    "0599999999": "abdallah"
}

def dircetory(phoneNumber):


     if phoneNumber.isdigit() and len(phoneNumber)==10 :
         if phoneNumber in telephone_directory:
             print(f" name: {telephone_directory[phoneNumber]}")
         else:
             print("Sorry, the number is not found ")
     else:
         print("This is invalid number")




def add(phone, name):
    if phone.isdigit() and len(phone) == 10:
        if phone in telephone_directory:
            print("Phone number is already added")
        else:
            telephone_directory.update({phone:name})
            print("Number added successfully!")
            print(telephone_directory)
    else:
        print("Invalid phone number")



def search_by_name(name):
    for phone,person in telephone_directory.items():
        if person==name:
            print(f"name:{name} ,phone:{phone}")
            return
    print("Sorry, the name is not found ")







print("________________________welcome to Telephone directory________________________")
dircetory(input("enter phone number: "))
name,phone=input("enter the name the phone number: ").split()
add(phone,name)
search_by_name(input("enter name: "))