# Python code to demonstrate string length  using len
str1=input("Enter the string to find the length")
print("The given string length :"+str(len(str1)))
########################################################
# Python code to demonstrate string length  using for loop
# Returns length of string
def finLen(str1):
    counter = 0
    for i in str1:
        counter += 1
    return counter

print("The length of the string using loops:"+str(finLen(str1)))
##############################################################
