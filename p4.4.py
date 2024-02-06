marks=int(input("Enter your marks: "))
if marks>=90: 
    print("A GRADE")
elif marks>=80 and marks<=89: 
    print("B GRADE")
elif marks>=70 and marks<=79:
    print("C GRADE")
elif marks>=60 and marks<=69: 
    print("D GRADE")
elif marks>50 and marks<=59:  
    print("E grade")
else: 
    print("FAIL")