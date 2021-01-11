# Python3 program to print  even length words in a string
def printword(s):
    s= s.split(' ')
    for word in s:
        if len(word)%2==0:
            print(word)

#drive code
s1=input("Enter the string to split even")
print("The splitted string"+ str(printword(s1)))