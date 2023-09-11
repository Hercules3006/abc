import math 
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return n>1
for i in range(int(input())):
    s=input()
    sum=0
    for i in range(0,len(s)):
        sum+=int(s[i])
    if isPrime(sum):
        print('YES')
    else:
        print('NO')