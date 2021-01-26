a=[100,50,10,5,2,1]
sum=0;
n=int(input())
for i in range(6):
       if(n>=a[i]):
           sum+=n//a[i];
           n=n%a[i];
print(int(sum))
