n=int(input())
b=list(map(int,input().split()))
a=list(map(int,input().split()))
i=1
if(a[0]>b[0]):
    c=0
else:
    c=1
for i in range(len(b)):
    if(b[i]-b[i-1]>=a[i]):
        c+=1
print(c)
