mylist=[]
newlist=[]
for i in range (1,10): 
    number=int(input("Enter a number: "))
    mylist.append(number)
print("list before deltion of duplicates\n")
print(mylist)

for i in mylist: 
    if i not in newlist: 
        newlist.append(i)
   

print("list after deltion of duplicates\n")
print(newlist)