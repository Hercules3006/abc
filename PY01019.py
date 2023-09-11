def check(a, b):
    for i in range(1, len(a)):
        if abs(ord(a[i]) - ord(a[i - 1])) != abs(ord(b[i]) - ord(b[i - 1])):
            return 'NO'
    return 'YES'
for i in range(int(input())):
    s=input()
    print(check(s,s[::-1]))