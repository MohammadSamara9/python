n1= float (input("enter the number one: "))
op=input("enter the operation type: ")
n2= float(input("enter the number two: "))


if op== "+":
    print(n1+n2)
elif op == "-":
    print(n1-n2)
elif op== "*":
    print(n1*n2)
elif op == "/":
    if n2!=0:
        print(n1/n2)
    else:
        print("error")
else:
    print("invalid operation")
