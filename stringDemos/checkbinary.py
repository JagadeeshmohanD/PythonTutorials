# Python program to check if a string is binary or not function for checking the string is accepted or not
def check(str1):
    p = set(str1)
    # set function convert string into set of characters .
    # declare set of '0','1'
    s ={'0','1'}
    if s == p or p == {'0'} or p == {'1'}:
        print("Given string is binary")
    else:
        print("Given string is not a binary")

#drive code
if __name__ == "__main__":
    str1 = input("Enter string for validation")
    check(str1)


