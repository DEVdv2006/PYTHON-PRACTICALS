import math
a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))

dicmrinant=(b*b)-4*a*c
x1=((-b-math.sqrt(dicmrinant))/2*a)
x2=((-b+math.sqrt(dicmrinant))/2*a)
print("Real roots are ",x1," ",x2)