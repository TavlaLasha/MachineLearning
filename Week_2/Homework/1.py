import random as rd
from collections import Counter

print("..........1.............")
numbs = [34, 11, 7, 23, 1]
print(sum(numbs))
print(min(numbs))
print(max(numbs))
print(sum(numbs) / len(numbs))
numbs.append(102)
numbs[2] = 205
numbs.pop(3)
numbs.sort()
print(numbs)

print("..........2.............")
nums = []
for i in range(1, 11):
    nums.append(int(input("Type Number {}: ".format(i))))
print(nums)

print("..........3.............")
fruits = ["Watermelon", "Apple", "Banana"]
fruits.sort(reverse=True)
print(fruits)

print("..........4.............")


def listMult(nums):
    answer = 1
    for num in nums:
        answer *= num
    return answer


print(listMult([2, 4, 1, 6]))

print("..........5.............")


def listOddPop(nums):
    for num in nums:
        if (num % 2 != 0):
            nums.remove(num)
    return nums


print(listOddPop([2, 4, 1, 6, 8]))

print("..........6.............")
numbs = [34, 11, 7, 23, 1]

for num in range(0, len(numbs)):
    numbs[num] += 10

print(numbs)

print("..........7.............")
nums = []
for i in range(1, 11):
    nums.append(rd.randint(25, 110))
print(nums)
print("Min is: {}".format(min(nums)))

print("..........8.............")


def comparison(a, b):
    for i in a:
        for k in b:
            if i == k:
                return True
    return False


a = [1, 2, 3, 4, 5]
b = [7, 4, 8, 9, 0]
print(comparison(a, b))

print("..........9.............")


def listOddPop(nums):
    for num in nums:
        if num % 2 != 0:
            nums.remove(num)
    return nums


print("..........10.............")

nums = []
for i in range(1, 11):
    nums.append(rd.randint(25, 110))
nums.sort()
rd.shuffle(nums)
print(nums)

print("..........11.............")
print(rd.choice(nums))

print("..........12.............")
numb = str(input("Type huge integer: "))
sums = 0
for n in numb:
    sums += int(n)
print(sums)

print("..........13.............")
numbs = [1, 5, 23, 5, 12, 2, 5, 1, 18, 5]
results = {}
for i in numbs:
    count = 0
    for k in numbs:
        if k == i:
            count += 1
    results.update({i: "repeats {} times".format(count)})
print(results)

print("..........14.............")
extensions = ['txt', 'jpg', 'gif', 'html']
file = str(input("Type File Name: "))
splitted = file.split(".")
extBool = False
print(len(splitted))
if len(splitted) == 2:
    for ending in extensions:
        if splitted[1] == ending:
            extBool = True
    if extBool:
        print("Yes")
    else:
        print("No")
else:
    print("Wrong file name")

print("..........15.............")
string = "python php pascal javascript java c++"
splittedString = string.split(" ")
print(splittedString)
maxStr = 0
maxString = ''
for i in splittedString:
    if len(i) > maxStr:
        maxStr = len(i)
        maxString = i
print("Biggest Word: {}".format(maxString))

print("..........16.............")
numbs = [1, 5, 23, 5, 12, 2, 5, 1, 18, 5]
numbs.sort()
n = len(numbs)

print(sum(numbs) / len(numbs))

if n % 2 == 0:
    median1 = numbs[n // 2]
    median2 = numbs[n // 2 - 1]
    median = (median1 + median2) / 2
else:
    median = numbs[n // 2]
print(median)

data = Counter(numbs)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))

print(get_mode)
