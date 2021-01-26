r = int(input())
sum=0
for i in range(1900,r):
        if((i%400==0)or ((i%4==0) and (i%100!=0))):
            sum+=366
        else:
            sum+=365
F=sum%7
if(F==0) :
          print("Monday")
elif(F==1) :
          print("Tuesday")
elif(F==2):
           print("Wednesday")
elif(F==3) :
         print("Thursday")
elif(F==4) :
         print("Friday")
elif(F==5) :
          print("Saturday")
else :
             print("Sunday")
