import math
def isPrime(s):
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0:
            return 'NO'
    return 'YES' if s>1 else 'NO'
for i in range(int(input())):
    s=input()
    n=int(s[-4:])
    print(isPrime(n))