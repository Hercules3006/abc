def solve(n):
    for i in range(0,len(n)-2):
        if (n[i]!=n[i+2]):
            return 'NO'
    return 'YES'
for i in range(int(input())):
    n=input()
    print(solve(n))