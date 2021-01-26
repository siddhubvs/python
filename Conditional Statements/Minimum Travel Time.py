import math
a=list(map(int,input().split()))
if(a[2]==0 or a[1]==0):
    if(a[2]==0):
        print("Stairs")
    elif(a[1]==0):
        print("Elevator")
else :
    t1=math.sqrt(2)*a[0]/a[1]
    t2=(a[0]*2)/a[2]
    if(t1<t2):
        print("Stairs")
    else:
        print("Elevator")
