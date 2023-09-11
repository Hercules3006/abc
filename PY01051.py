for i in range(int(input())):
    s=input()
    sum=0
    for i in range(0,len(s)):
        sum+=int(s[i])
    s1=str(sum)
    if len(s1)>1 and s1==s1[::-1]:
        print('YES')
    else:
        print('NO')