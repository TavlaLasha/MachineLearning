print('..........1...........')
print('a)',9-3)
print('b)',8*2.5)
print('c)',9/2)
print('d)',9/-2)
print('e)',9//-2)
print('f)',9%2)
print('g)',9.0%2)
print('h)',9%2.0)
print('i)',9%-2)
print('j)',-9%2)
print('k)',9/-2.0)
print('l)',4+3*5)
print('m)',(4+3)*5)

print('..........2...........')
print(4-pow(2,3)+5*2-3/2)

print('..........3...........')
print('a)', (3+245)*4-pow(3,4))
x = (42+3*3)/2+4
print('b)', x ,'and', int(x))

print('..........5...........')
text = "What's up, doc?"
print(text)

print('..........6...........')
a=1
b=4
print("a=",a,"b=",b)
a,b=b,a
print("a=",a,"b=",b)

print('..........7...........')
x, y = 2, 6
x, y = y, x + 2
print(x, y)

print('..........8...........')
fname=input("First Name: ")
lname=input("Last Name: ")
print(fname,lname)

print('..........9...........')
num=int(input("Number:"))
print("{0:b}".format(num))

print('..........10...........')
time=int(input("Work Time:"))
wage=int(input("Wage Per Hour:"))
print("Monthly wage:", time*wage*30)

print('..........11...........')
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
print((a+b+c)/3)

print('..........12...........')
name=input("Name: ")
age=int(input("Age: "))

print(name,"tqven gaxdebit 100 wlis", 100-age, "weliwadshi")

print('..........13...........')
num=float(input("Degree:"))
info = input("Celsius or Fahrenheit? (Celsius -> C, Fahrenheit -> F")
if info=="C" or info=="c":
    print(num," degree Celsius is", (num*9/5)+32)
elif info=="F" or info=="f":
    print(num," degree Fahrenheit is", (num-32)*5/9)
else:
    print("Wrong info")
