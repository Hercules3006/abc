import math
def check(x, y):
    a, b=int(x), int(y)
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    if  a==1:
        return 'YES'
    else :
        return "NO"

for i in range(int(input())):
    s=input()
    print(check(s,s[::-1]))