num=[]
unique=[]
str=input("enter a string :")
for i in str: 
    if i=='0' or i=='1' or i=='2' or i=='3':
        if i not in unique: 
          print(f"{i} comes {str.count(i)}")
          unique.append(i)
# for i in num:
 
#     print(f"{i} comes {num.count(i)} time")