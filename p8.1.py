import random
def shuffle(list):
    random.shuffle(mylist)
    print(mylist)
mylist=[]
while True: 
    element=input('enter an element to the list:')
    if element=='break': 
        break
    mylist.append(element)

print("list before shuffling\n")
print(f"{mylist}\n")
print("list after shuffling\n")
shuffle(mylist)
