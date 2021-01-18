# Python3 program for removing i-th  indexed character from a string
# Removes character at index i
def remove(string,i):
    a=string[:i]
    b=string[i+1:]
    return a+b

#driving code
if __name__ == '__main__':
    string = input("Enter the string for validation")
    i = int(input("Enter the value of i"))
    print(remove(string,i))
