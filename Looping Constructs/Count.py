n = int(input())
o=e=0
l=list(map(int,input().split()))
for i in l :
    if(i%2==0) : o+=1
    else : e+=1
print(o,e)
