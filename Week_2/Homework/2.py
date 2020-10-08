print("..........1.............")
mydict = {0: 10,1: 20}
mydict.update({2:14, 3:45})
print(mydict)
mydict.pop(2)
print(mydict)

print("..........2.............")
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic = {**dic1, **dic2, **dic3}
print(dic)

print("..........3.............")
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
if 3 in d:
  print("Yes, 3 is one of the keys in the d dictionary")

print("..........4.............")
d = {'x': 10, 'y': 20, 'z': 30}
for i in d:
    print('{} -> {}'.format(i, d[i]))

print("..........5.............")
diction={}
for i in range(1,11):
    diction[i]=pow(i,2)

print(diction)

print("..........7.............")
myset = {0,1,2,3,4}
myset.update([5,6,7])
myset -= {0,1}

for i in myset:
    print(i)
print("Length: ",len(myset))

print("..........8.............")
set1 = {"green", "blue"}
set2 = {"blue", "yellow"}

print("..........10.............")
mylist = []
for i in range(1, 101):
    if i%5==0:
        mylist.append(pow(i,3))
mytuple = tuple(mylist)
print(mytuple)
print("Mytuple length: ",len(mytuple))
