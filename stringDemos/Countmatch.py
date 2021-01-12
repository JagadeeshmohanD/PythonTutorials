# count function count the common unique characters present in both strings .
def count(str1,str2):
    # set of characters of string1
    set_string1 = set(str1)
    # set of characters of string2
    set_string2 = set(str2)
    matched_characters = set_string1 & set_string2
    print("No. of matching character are :"+ str(len(matched_characters)))

#driver code
if __name__ == "__main__":

    str1 = input("Enter first string for character count")
    str2 = input("Enter second string for character count")
    count(str1,str2)

#################################################################
# Count the Number of matching characters in  a pair of string
import re
c = 0
for i in str1:
    if re.search(i,str2):
        c=c+1
print("No of matching character are",c)
