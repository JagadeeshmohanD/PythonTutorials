# Python3 program to check if a string contains any special character
import re
def run(str1):
    regex = re.compile('[@_!#$%&*()<>?/\|{}~:]')
    if(regex.search(str1)== None):
        print("String doesnt have special character and Accepted")
    else:
        print("String have special character and not Accepted")


#drive code
if __name__ == '__main__' :
    str1 = input("Enter the string for regex validation")
    print("The Given string is :"+ str1)
    run(str1)