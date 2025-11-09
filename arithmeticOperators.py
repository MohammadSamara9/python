x1=2+3
x2=9-2
x3=x2*x1
x4=x3/x1
x5=x3%x1
print(x1,x2,x3+1,x4,x5)
x2+=1
x2-=3
print(x1,x2,x3,x4,x5)


result1=x1==5
print(result1)
result2=x3<=x1
print(result2)
result3=x2>=x1
print(result3)
result4=x5!=x1
print(result4)


logic=result1 and result2
print(logic)
logic=result1 and result3
print(logic)
logic=result1 and result2
print(logic)
logic=result1 and result4
print(logic)





