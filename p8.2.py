def removeDuplicate(list):
    newlist=[]
    for i in range(0,len(list)): 
            if list[i] not in newlist:
                newlist.append(list[i]) 
    return newlist
  
mylist=[]
while True: 
    element=input('enter an element to the list:')
    if element=='break': 
        break
    mylist.append(element)

x=removeDuplicate(mylist)
print(x)