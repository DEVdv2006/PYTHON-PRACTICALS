positive=0
negative=0
even=0
odd=0
avg=0
sum=0
number=[]
n=int(input("Enter number you want to add in list\n"))
for i in range(1,n+1): 
    num=int(input("Enter number"))
    number.append(num)

for i in  number: 
    if i%2==0: 
        even=even+1 
    if i%2!=0: 
        odd=odd+1
    if i>0: 
        positive=positive+1
    if i<0: 
        negative=negative+1
    sum=sum+i

avg=sum/n
print(f"+VE NUMBERS:{positive}")
print(f"-VE NUMBERS:{negative}")
print(f"Even NUMBERS:{even}")
print(f"Odd NUMBERS:{odd}\n")
print(f"Average of all NUMBERS:{avg}\n")