n=int(input())
a=30
b=35
i=0
while n!=0:
    a+=8*i
    n-=1
    print(a," ",sep='',end='')
    if n==0:exit()
    b+=6*i
    n-=1
    print(b," ",sep='',end='')
    i+=1
