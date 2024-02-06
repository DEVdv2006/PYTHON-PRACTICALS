year=int(input("enter a year to check wether it is leap or not:"))
# leap year if perfectly divisible by 400
if year%400==0: 
    print("YEAR IS LEAP")
# not a leap year if divisible by 100
# but not divisible by 400
elif year%100==0:   
    print("NOT A LEAP YEAR")
# leap year if not divisible by 100
# but divisible by 4
elif year%4==0: 
     print("YEAR IS LEAP")
else: 
    print("NOT A LEAP YEAR")