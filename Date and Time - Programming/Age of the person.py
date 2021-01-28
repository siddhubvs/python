import datetime
from datetime import datetime
a=list(map(int,input("Enter Birth date as mm/dd/yyyy format:").split("/")))
b=list(map(int,input("Enter Current date as mm/dd/yyyy format:").split("/")))
c=b[2]-a[2]
c=c-1 if b[1]<a[1] or b[1]==a[1] and b[0]<a[0] else c
print("The current age of the person is ",c)
