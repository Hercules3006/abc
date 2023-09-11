for i in range(int(input())):
    S=input()
    inx=S[0]
    cnt=0
    res=''
    s=S+' '
    for i in range(0,len(s)):
        if s[i]==inx:
            cnt+=1
        elif s[i]!=inx:
            res+=str(cnt)+inx
            cnt=1
        inx=s[i]
    print(res)