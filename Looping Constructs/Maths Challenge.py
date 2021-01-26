k=int(input())
n=int(input())
streak=0
for i in range(1,n):
    j=1
    while(i%j==0) : j+=1
    if(j-1==k)    : streak+=1
print(streak)
