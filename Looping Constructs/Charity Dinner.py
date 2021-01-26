x=0
y=99999
p=int(input())
g=int(input())
r=int(input())
o=int(input())
n=int(input())
i=0
while (i*p<=n) :
        j=0
        while(j*g<=n):
            k=0
            while(k*r<=n):
                l=0
                while(l*o<=n) :
                    if((o*l+r*k+g*j+p*i)==n) :
                
                        if((i+j+k+l)<y) : y=i+j+k+l
                        x+=1
                        print("# of PINK is",i,"# of GREEN is",j,"# of RED is",k,"# of ORANGE is",l)
                
                    l+=1
                k+=1    
            j+=1    
        i+=1    
print("Total combinations is",x)
print("Minimum number of tickets to print is",y)
