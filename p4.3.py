weight=int(input("Enter your weight in Kgs: "))
height_in_cm=int(input("Enter your height in cms:"))
height_in_metre=(height_in_cm)/100

bmi=(weight)/(height_in_metre*height_in_metre)
if bmi>=19 and bmi<25: 
    print("you have normal bmi your bmi is ",bmi)
elif bmi<19:
    print("you have underweight bmi your bmi is ",bmi)
else:  
    print("you have overweight bmi your bmi is ",bmi)