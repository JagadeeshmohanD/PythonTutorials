# function to check if small string is  there in big string
# def check(string, sub_str):
#     if (string.find(sub_str) == -1):
#         print("String not present")
#     else:
#         print("string present")
#
# #driving code
# string = input("Enter the main string")
# sub_string = input("Enter the substring to search")
# check(string,sub_string)
####################################################
#using count method
def check1(s2,s1):
    if(s2.count(s1)>0):
        print("String Present")
    else:
        print("String not present")

#driving code
s2=input("Enter the main string s2 for verification")
s1=input("Enter the sub string s1 for verification")
check1(s2,s1)
