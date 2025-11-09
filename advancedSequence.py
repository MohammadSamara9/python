#indexing
from xml.dom.minidom import ProcessingInstruction

alphabet="abcdefghijklmnopqrstuvwxyz"
the_list=[99,45,34,12]
the_tuple=(67,89,45,25)
print(alphabet[0])
print(alphabet[-1])
print(the_list[-2])
print(the_tuple[-4])


print(alphabet.index("m"))
print(the_list.index(34))

#slicing
text="this is pyhon course"
print(text[8:14])
print(text[8:])
print(text[:14])
print(text[:])
print(text[-6:])
print(the_tuple[1:])
print(the_list[:-1])
print(alphabet[0:7:2])
print(alphabet[7:0:-1])
print(alphabet[0::6])

s=slice(0,10,2)
print(text[s])

#in
print("is" in text)
print("IS" in text)
print("is"not in text)
print("IS" not in text)
print(99 in the_list)

#Built-in and redundant
first_name=" mohammed"
second_name="samara"
print(first_name*3 + " " + second_name)
print(the_list+the_list)
print(the_tuple+the_tuple)

#find

print(text.find("py"))
print(text.find("PY"))
print(text.find("s"))
print(text.rfind("s"))
print(text.find("s",10,20))

#text to string
print(text.split())
print(text.split("s"))
print(text.split(" ",1))

#list to string
list_two=["a","b","c"]
print("".join(list_two))
print(" ".join(list_two))
print("/".join(list_two))

#chek string
value="78nsa3"
print(value.isalnum())
value="78n sa3"
print(value.isalnum())
num="9738434"
print(num.isdigit())

#replace
text_two="hi/nmohammed/nsamara/nhow/nare/nyou"
print(text_two.replace("/n"," "))


#edit string
str="tHIS iS the PYThON"
print(str.lower())
print(str.upper())
print(str.swapcase())
print(str.title())

#raw string
file_path=r"C:\Users\12411\Desktop\python\advanced\Sequence.py"
file_path2=R"C:\Users\12411\Desktop\python\advancedSequence.py"
file_path3="c:\\Users\\12411\\Desktop\python\\advancedSequence.py"

print(file_path)
print(file_path2)
print(file_path3)

#format
age=20
print("hi {} {} ,you are {} years old".format(first_name,second_name,age))
print("hi {1} {0} ,you are {2} years old".format(first_name,second_name,age))
print("hi {fname} {sname} ,you are {age} years old".format( fname=first_name,sname=second_name,age=age))