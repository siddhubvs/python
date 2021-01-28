f=int(input())
i=[input().split() for a in range(f)]
b={i[a][0]:list(map(int,i[a][1:])) for a in range(len(i))}
a=input()
for f,c in b.items():
	if a==f:
		print("Average Mark of is : %.2f" %(sum(c)/3))
