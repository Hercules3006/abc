import math
def check(s):
    for i in range(len(s)):
        if i%2!=0:
            if int(s[i])!=0:
                return True
    return False 
def cal(s):
    tich=1
    sum=0
    for i in range(len(s)):
        if i%2==0:
            sum+=int(s[i])
        else:
            if int(s[i])!=0: 
                tich*=int(s[i])
    if check(s)==False:
        tich=0
    print(str(sum)+" "+str(tich))
for i in range(int(input())):
    s=input()
    cal(s)