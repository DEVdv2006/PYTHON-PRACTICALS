n=1
while n<=10000:
    sum=0
    for i in range(1,n): 
        if n%i==0: 
            sum=sum+i 
        
    if sum==n: 
        print(n)
    
    n=n+1