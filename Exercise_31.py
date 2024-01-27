def me():
    poosh = inp.split(' ')
    poosh.sort(key=lambda x: int(x[1:]))
    for i in poosh:
        print(i[0],end='')
inp=str(input())
me()