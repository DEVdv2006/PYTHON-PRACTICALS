n=int(input("Enter total numbers for which you want to find average: "))
avg=0
sum=0
for i in range(n+1): 
    num =int(input("Enter Number: "))
    sum=sum+num
avg=sum/n
print("Average of numbers is ",avg)    
