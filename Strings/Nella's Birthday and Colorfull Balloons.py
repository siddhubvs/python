ma=mb=0
s=input()
for i in range(len(s)):
    if(s[i]=='a'):ma+=1
    else:mb+=1
if(ma<mb):mb=ma
print(mb)
