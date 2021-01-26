p=0
s=0
for i in range(0,3) :
     print("Enter the number of people who watched show",(i+1))
     a = input()
     print("Enter the average rating for show",(i+1))
     b = input()
     a=float(a)
     b=float(b)
     s+=(a*b)
     p+=a
print("The overall average rating for the show is","{:.2f}".format((s/p)))
