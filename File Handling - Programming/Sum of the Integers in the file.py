fhand=open("sample.txt","r")
sum=0
for line in fhand:
        words = line.split()
        for i in words:
           if(i.isdigit()):
                    sum=sum+int(i)
print("The sum of the integers in the file {} is:{}".format(fhand.name,sum))
