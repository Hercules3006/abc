import math
def check(s):
    for i in range(len(s)-1):
        if abs(ord(s[i])-ord(s[i+1]))!=2:
            return 'NO'
    if sum(int(i) for i in s) %10!=0:
        return 'NO'
    return 'YES'
for i in range(int(input())):
    s=input()
    print(check(s))

