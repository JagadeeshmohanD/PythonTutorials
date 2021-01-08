# Python code to demonstrate method to remove i'th character Naive Method
# Removing char at pos 3 using loop
def removei(test_str):
    new_str = ""
    for i in range(len(test_str)):
        if i !=2:
            new_str = new_str+test_str[i]
    return new_str

#printing string after removal
#def code
givenstr = input("Enter string removal")
print("The given string before removal:"+givenstr)
new_remove = removei(givenstr)
print("The string after removal of i th character :"+ new_remove)