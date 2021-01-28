def findType(a):
    m=0
    for i in range (1,(a//2)+1):
        if(a%i==0): m+=1
    m+=1    
    if(m==4) :  return 1
    return 0
a=int(input())
b=findType(a)
#print(b)
print("Nice" if(b==1) else "Not Nice")
