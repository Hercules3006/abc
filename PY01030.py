import math
def gcd(n,i):
    while n!=i:
        if n>i:
            n-=i
        else:
            i-=n
    if n==1:
        return True
    else:
        return False

    

n,k = [int(i) for i in input().split()]
a=10**k
b=10**(k-1)
cnt=0
for i in range(b,a):
    if(gcd(n,i)):
        print(i,end=" ")
        cnt+=1
        if cnt%10==0:
            print()

