print("..........1.............")
num = float(input("Number: "))
if num > 0:
    print("Number is positive")

print("..........2.............")
num = float(input("Number: "))
if num%10==0:
    print("Number ends with 0")
else:
    print("Number does not ends with 0")

print("..........3.............")
num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))

if num1>10 and num2 >10:
    print((num1+num2)/2)
else:
    print(num1*num2)

print("..........4-5.............")
num = float(input("Number: "))

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number equals to zero")

print("..........6.............")
num = input("Number: ")
print(num[-1])

print("..........7.............")

print("..........1.2.............")
for i in range(5, 126):
    if i%5==0:
        print(i)

print("..........2.2.............")
for i in range(200, 25, -1):
    if i%8==0:
        print(i)

print("..........3.2.............")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

if num1 > num2:
    for i in range(1, num1):
        if num1%i==0 and num2%i== 0:
            print(i)
else:
    for i in range(1, num2):
        if num1%i==0 and num2%i== 0:
            print(i)

print("..........4.2.............")
num=0
for i in range(1,11):
    num+=i
print(num/10)

print("..........5.2.............")
count=0
for i in range(1,101):
    if i%2==0:
        count+=1
print(count)

print("..........6.2.............")
for i in range(1500,2101):
    if i%7==0 and i%5==0:
        print(i)

print("..........7.2.............")
sum=0
for i in range(1500,2101):
    if i%7==0 and i%5==0:
        sum+=i
print(sum)

print("..........8.2.............")
sum=0
for i in range(1500,2101):
    if i%7==0 and i%5==0:
        sum+=i
        if sum >= 20000:
            break
print(sum)

print("..........9.2.............")
count=0
for i in range(1500,2101):
    if i%5==0:
        count+=1
print(sum)

print("..........10.2.............")
for i in range(15,151):
    if i%5==0:
        if i==50 or i==75 or i==80:
            continue
        else:
            print(i)

print("..........11.2.............")
