n0=n1=0
s=input()
for i in range(len(s)):
    if(s[i]=='0'):n0+=1
    else:n1+=1
if(n0==1 or n1==1):
    print("Yes")
else:
    print("No")
