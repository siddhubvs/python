a,b,c=map(int,input().split())
g= 10 if(a > 50 and b>60 and c > 100) else 9 if(a > 50 and b>60) else 8 if(b>60 and c > 100) else 7 if(a>50 and c > 100) else 6 if(a > 50 or b>60 or c > 100) else 5
print(g)
