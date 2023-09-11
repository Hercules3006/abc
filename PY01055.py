def check(s):
    if len(s)%2==0:
        return 0
    if s[0]==s[1]:
        return 0
    for i in range(0,len(s)-1,+2):
        if s[0]!=s[i]:
            return 0
    return 1
for i in range(int(input())):
    s=input()
    if check(s):
        print('YES')
    else:
        print('NO')
        