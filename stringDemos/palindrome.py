# function which return reverse of a string
def isPalindrome(s):
    return s == s[::-1]

#driving code
s=input("Enter string to verify palindrome")
ans = isPalindrome(s)
if ans:
    print("Given String is palindrome")
else:
    print("The Given string in not palindrome")

######################################################
# Using predefined function to reverse to string print(s)
def isPalindrome1(s1):
    rev = ''.join(reversed(s1))
# Checking if both string are equal or not
    if(s1 == rev):
        return True
    return False

#driving code
s1 = input("Enter string to verify palindrome ")
pal = isPalindrome1(s1)

if(pal):
    print("Given String is palindrome")
else:
    print("Given String is not palindrome")

