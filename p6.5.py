import random
mylist=[]

for i in range(0,4):
    mylist.append([]) 
    for j in range(0,4): 
        mylist[i].append(random.randint(0,1))
        
    
for i in range(0,4): 
    for j in range(0,4): 
            #mylist.append(random.randint(0,1))
        print(mylist[i][j],end=" ")
    print()
#print(mylist)

max_row_index = max(range(len(mylist)), key=mylist.__getitem__)
print(f"Row with the most 1s: {max_row_index}")

# Find the column with the most 1s
column_sums = [sum(col) for col in zip(*mylist)]
max_column_index = max(range(len(column_sums)), key=column_sums.__getitem__)
print(f"Column with the most 1s: {max_column_index}")