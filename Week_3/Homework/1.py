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

print("............9.............")
def comparison(a,b):
    for i in a:
        for k in b:
            if i==k:
                return True
                break
    return False

a = [1,2,3,4,5]
b = [7,4,8,9,0]
print(comparison(a,b))