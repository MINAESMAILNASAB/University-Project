def dis(a, b):
    t = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            t = t + 1
    return t

n = int(input())
import re
text = input().strip()
text = re.sub('[؟،:؛.\']+', '', text)
wrd = input()
lst = text.split(' ')
for item in lst:
    t = wrd
    tmp = ""
    d = len(item) - len(wrd)
    for i in range(d):
        tmp = tmp + "_"
    t = t + tmp
    a = dis(item, t)
    if n >= a:
        print(item)