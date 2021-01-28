x=input()
y=input()
for i in range(len(x)):
    if(x[i]==y[i]):
        if(x[i]=="B"):
            print("W",end='')
        else:
            print("B",end='')
    else:
        print("B",end='')
