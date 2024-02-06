#1) ram_age=int(input("enter rams age"))
# sam_age=int(input("enter sams age"))
# khan_age=int(input("enter khans age"))

# eldest=ram_age if (ram_age>sam_age and ram_age>khan_age) else sam_age if (sam_age>ram_age and sam_age>khan_age) else khan_age
# youngest=ram_age if (ram_age<sam_age and ram_age<khan_age) else sam_age if (sam_age<ram_age and sam_age<khan_age) else  khan_age
# print(eldest)
# print(youngest) 

# 2)num=int(input("enter num:"))
# res= 'even' if num%2==0 else 'odd'
# print(f"{num} is {res}")

# 3)largest=0
# while True: 
#     user_input=input('Enter a number')
#     if user_input.lower()=='done':
#           break
#     else: 
#          number=int(user_input)
#          if number > largest: 
#              largest=number
            
#          print(f"Largest number is {largest} ")


#4) def fibo(n): 
#      if n<=1: 
#          return n
#      else: 
#          return fibo(n-1)+fibo(n-2)
    
# num=int(input("Enter num: "))
# for i in range(1,num+1):  
#      print(fibo(i))  

# num=int(input("Enter num:"))
# temp=num
# remainder=0
# reverse=0
# while temp>0: 
#     remainder = temp%10
#     reverse = reverse*10+remainder
#     temp=temp//10
# if num==reverse: 
#     print('palindrome')
# else: 
#     print('not palindrome')
    
# for i in range(1,6): 
#     for j in range(1,i+1): 
#         print(i,end=' ')
#     print(' ')

# l1=[1,22,3,4,5]
# l2=[1,2,3,4,5]
# def is_sorted(list):
#     flag=0 
#     for i in list: 
#         if list[i]>list[i+1]: 
#              print('list is not sorted')
#              flag=1
#              break
#     if flag==0: 
#         print('list is sorted')
        
# is_sorted(l1)
# is_sorted(l2)

l1=[1,2,3,4,5,67,1,11]
if l1[0]==l1[len(l1)-1]: 
    print('first and last are same')
else: 
    print('first and last are not same')
