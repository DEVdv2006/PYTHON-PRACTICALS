number=[]
for i in range(1,11): 
    num=int(input("Enter number"))
    number.append(num)
    
for i in range(len(number)): 
        for j in range(i+1, len(number)):
            print(number[i], number[j])