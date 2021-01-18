# Python program to find all string which are greater than given length k
# function find sttring greater than length k
def stringGreater(k,str):
    string =[]
    text = str.split(" ")
    for x in text:
        if len(x) > k:
            string.append(x)
    return string

#driving program
k = int(input("Enter the value of K"))
str= input("Enter the string for vallidation")
print(stringGreater(k,str))