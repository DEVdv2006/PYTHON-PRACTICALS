j=1
sum=0
for i in range(3,100):
    if i%2!=0: 
       sum=sum+ (j/i)
       j=j+2
print(sum)
