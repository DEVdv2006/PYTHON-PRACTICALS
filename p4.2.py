hour=int(input("Input hours of work"))
hourlyRate=int(input("Enter hourly rate"))
wage=0
if hour>40:  
    wage=((hour-40)/2)*hourlyRate

print("your wage is ",wage," this week")    