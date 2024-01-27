adad = input()
motghayer = int(input())
numlist= adad.split()
dict1 = dict()
findict = dict()
for index,item in enumerate(numlist):
    dict1[int(item)]=index

for i in dict1.keys():
    tlt = motghayer - i
    if tlt in dict1 and tlt!=i:
        jam1 = dict1[i]+dict1[tlt]
        if (tlt,i) not in findict.keys():
            findict[(i,tlt)]=jam1
finalres = sorted(findict.values())
if not findict:
    print("Not Found!")

else:
    for k in finalres:
        print(k)