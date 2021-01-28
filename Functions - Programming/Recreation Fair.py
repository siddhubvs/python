def fa(a,b):
     t=a if a<b else b
     m=1
     for i in range (1,t+1):
        if(a%i==0 and b%i==0) : m=i
     return m
a=int(input())
b=int(input())
print(fa(a,b))
