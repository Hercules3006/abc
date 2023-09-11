import math 
def check(n):
    if n%3!=0:
        return 0
    else:
        return 1
for i in range(int(input())):
    s=input()
    sum=0
    for i in range(0,len(s)):
        sum+=int(s[i])
    if check(sum):
        print('YES')
    else:
        print('NO')