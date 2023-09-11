import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return n>1
for i in range(int(input())):
    s=input()
    nt=0
    for i in range(len(s)):
        if isPrime(int(s[i])):
            nt+=1
    if isPrime(int(len(s))) and nt>(int(len(s))-nt):
        print('YES')
    else:
        print('NO')