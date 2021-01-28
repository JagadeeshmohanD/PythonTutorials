# Python program to split a string and join it using different delimiter
def split_string(str1):
    list_string = str1.split(' ')
    return list_string

def join_string(list_string):
    str1 = '-'.join(list_string)
    return str1

#driver function
if __name__ == '__main__':
    str1 = input("Enter the string split and join")

    #splitting a string
    list_string = split_string(str1)
    print(list_string)

    #join list of strings into one
    new_string = join_string(list_string)
    print(new_string)