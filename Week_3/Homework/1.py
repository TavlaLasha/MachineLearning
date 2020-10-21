# import sys
# sys.path.append("NumPy_path")
# import NumPy
import numpy

print("............1.............")
def numAvg(num1, num2):
    return (num1+num2)/2
print(numAvg(3, 6))
print(numAvg(10, 26))

print("............2.............")
def numAvg2(num1, num2):
    print((num1+num2)/2)

numAvg2(3, 6)
numAvg2(10, 26)

print("............3.............")
def power(num1):
    return pow(num1, 3)
print(power(3))
print(power(10))

print("............4.............")
def minNum(num1, num2):
    print(min(num1, num2))

minNum(3, 6)
minNum(10, 26)

print("............5.............")
def oddEven(num1):
    if(num1%2==0):
        return False
    else:
        return True
print(oddEven(3))
print(oddEven(10))

print("............6.............")
def fact(num):
    if(num<=0):
        print("Factorial can not be calculated for ", num)
    else:
        fact = 1
        for i in range(1,num+1): 
            fact = fact * i 
            
        print ("The factorial of {} is : {}".format(num, fact)) 
    
fact(1)

print("............7.............")
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num-1))

num = 5
print("The factorial of", num, "is", factorial(num))

print("............8.............")
numbs = [1, 2, 3, 4, 5]
print(sum(numbs))
print(min(numbs))
print(max(numbs))
print(sum(numbs)/len(numbs))
numbs.append(102)
numbs[2]=205
numbs.pop(3)
numbs.sort()
print(numbs)

print("............9.............")
def comparison(a, b):
    for i in a:
        for k in b:
            if i == k:
                return True
    return False

a = [1, 2, 3, 4, 5]
b = [7, 4, 8, 9, 0]
print(comparison(a, b))

print("............10.............")
arr1 = numpy.array([1, 5, 8, 4, 5])
arr2 = numpy.array([6, 7, 5, 3, 9])
print(arr1+arr2)

print("............1.1.............")
numbs = []
for i in range(20, 126):
    if(i%5==0):
        numbs.append(i)
print(numbs)

print("............1.2.............")
numbs = []
for i in range(20, 126):
    if(i%8==0):
        numbs.append(i)
numbs.sort(reverse=True)
print(numbs)

print("............1.3.............")
def numConf(num1, num2):
    if(num1>num2):
        sameDivider(num2, num1)
    elif(num1<num2):
        sameDivider(num1, num2)
    else:
        sameDivider(num1, num1)

def sameDivider(x, y):
    dividers= []
    for i in range(1, y+1):
        if(x % i == 0 and y % i == 0):
            dividers.append(i)
    print(dividers)

numConf(15,10)
numConf(50,50)

print("............1.4.............")
nums=[]
for i in range(1, 11):
    nums.append(int(input("Type Number {}: ".format(i))))
print(sum(nums)/len(nums))

print("............1.5.............")
sum=0
for i in range(1, 101):
    if (i%2==0):
        sum+=i
print(sum)

print("............1.6.............")
nums=[]
for i in range(1500, 2101):
    if (i%5==0 and i%7==0):
        nums.append(i)
print(nums)
