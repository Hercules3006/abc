import re 
for i in range(int(input())):
    s=input()
    s1=input()
    index=s.find(s1)
    cnt=0
    n=len(s1)
    while index!=-1:
        cnt+=1
        index=s.find(s1,index+n )
    print(cnt)
  