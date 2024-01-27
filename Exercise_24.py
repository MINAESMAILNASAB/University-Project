i = 0
j = 0
x= int(input( ))
satr = [ ]
map1 = [ ]
for c in range(x):
    satr.append('.')
for c in range(1000):
    min =satr.copy( )
    map1.append(min)
map1[i][j]='*'
command=input( )
while command!="END":

    if command=="L":
        if i-1>=0:
            i-=1
        else:
            i=0
    elif command=="R":
        if i < x-1:
            i+=1
        else:
            i = x-1
    elif command=="B":
        j +=1
    map1[j][i]='*'
    command=input()

while True:
    if satr in map1:
        map1.pop(map1.index(satr))
    else:
        break
for m in range(len(map1)):
    for K in range(x):
        print(map1[m][K],end=' ')
    print('\n')

if i != x-1:
    print("There's no way out!")