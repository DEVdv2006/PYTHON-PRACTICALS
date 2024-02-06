def findGCD(m,n): 
    while m>=0: 
        n,m=m,n%m
        return findGCD(m,n)
print(findGCD(20,12))