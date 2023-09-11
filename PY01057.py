import math 
def isPrime(s):
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0:
            return 0
    return s>1

def check(s):
    for i in range(0,len(s)):
        if (isPrime(i) and not isPrime(int(s[i])) or not isPrime(i) and isPrime(int(s[i]))):
            return 'NO'
    return 'YES'
for i in range(int(input())):
    s=input()
    print(check(s))