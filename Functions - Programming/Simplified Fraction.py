def findType(a,b):
    if(a%b==0) : print(a//b)
    else:
     t=a if a<b else b
     m=1
     for i in range (1,t+1):
        if(a%i==0 and b%i==0) : m=i;
     a//=m
     b//=m
     if(a>b) : print(a//b," ",a%b,"/",b,sep='')
     else :print(a,"/",b,sep='')
a=int(input())
d=int(input())
findType(a,d)
