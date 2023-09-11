s=input()
l=0
for i in s:
    if i.islower():
        l+=1
if l>= len(s)-l:
    print(s.lower())
else:
    print(s.upper())