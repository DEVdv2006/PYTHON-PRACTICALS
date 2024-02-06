def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = input('enter a string')
ans = isPalindrome(s)
 
if ans:
    print("string is palindrome")
else:
    print("string is not palindrome")