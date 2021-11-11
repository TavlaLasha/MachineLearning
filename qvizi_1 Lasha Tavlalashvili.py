import random as rd

print("----------1--------------")
mydict = {}
randnum = rd.sample(range(1, 100), 10)

for i in range(0, 10):
    choice = randnum[i]
    sp = str(choice)
    if len(sp) < 2:
        summary = choice
    elif len(sp) > 2:
        summary = int(sp[0]) + int(sp[1]) + int(sp[2])
    else:
        summary = int(sp[0]) + int(sp[1])
    mydict[choice] = summary

print(mydict)

print("----------2--------------")
mylist = []
for i in range(1, 21):
    mylist.append(rd.randint(5, 15))
print(mylist)

count = 0
save = ''
thisdict = {i: mylist.count(i) for i in mylist}
biggest = []
for key in thisdict:
    if thisdict[key] > count:
        count = thisdict[key]
        if save != key:
            biggest.clear()
        biggest.append(key)
        save = key
    print("{} repeated {} times".format(key, thisdict[key]))
if len(biggest) > 1:
    print("ყველაზე ხშირად გამეორდნენ: ")
    for i in biggest:
        print(i)
else:
    print("ყველაზე ხშირად გამეორდა: ", biggest[0])

print("----------3--------------")
gelist = "აბგდევზთიკლმნოპჟრსტუფღყშცძწხჯჰ"
strlist = []
for k in range(1, 21):
    randn = rd.randint(5, 15)
    chs = rd.choices(gelist, k=randn)
    fin = ''
    for i in chs:
        fin += i
    strlist.append(fin)

print(strlist)

bigxmovani = ''
prev = 0
for i in strlist:
    count = 0
    for k in i:
        if k in ["ა", "ე", "ი", "ო", "უ"]:
            count += 1
    if count > prev:
        prev = count
        bigxmovani = i

print("ყველაზე მეტი ხმოვანია {} სიტყვაში. ხმოვანების რაოდენობა {}".format(bigxmovani, prev))
