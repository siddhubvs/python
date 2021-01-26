import math
r= int(input())
a1,b1=map(int,input().split())
a2,b2=map(int,input().split())
a3,b3=map(int,input().split())
if(math.pow((a1-a2),2)+math.pow((b1-b2),2)>r*r):
       print("No")
elif(math.pow((a2-a3),2)+math.pow((b2-b3),2)>r*r):
       print("No")
else :       
    print("Yes")
