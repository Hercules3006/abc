import math
def so_nam(n,x,m):
    n+=n*x
    return n 

for t in range(int(input())):
    n,x,m = [float(i) for i in input().split()]
    # cthuc m=n*(1+x%)^res
    k=0
    while n<m:
        k=k+1
        so_nam(n,x,m)
    #res=math.log(m/n,1+x/100)
    #print(math.ceil(res))
    print(k)