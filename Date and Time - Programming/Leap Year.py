day,mon,year=map(int,input('Enter the date in format(dd/mm/yyyy)').split('/'))
if year%400==0 or (year%100==0  and year%4!=0) :
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")
