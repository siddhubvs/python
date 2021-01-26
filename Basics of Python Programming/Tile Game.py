import math
s=int(input("Enter the side in cm of a square tile\n"))
    
n=int(input("Enter the number of square tiles available\n"))
    
a=int(math.sqrt(n))
print("Area of the largest possible square is {}sqcm\n".format((a*a)*(s*s)))
