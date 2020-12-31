lst = []
def reverse(lst):
    lst.reverse()
    return lst

n = int(input("enter input of elements in list []"))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print(lst)
print(reverse(lst))

########################################################
lst1: str=[]
def reversestr(lst1):
    if len(lst1) == 0:
        return lst1
    else:
        return reversestr(lst1[1:])+lst1[0]


lst1 = str(input("enter the sting for reversal"))
print(lst1)
print("The reversed string using recursion is ")
print(reversestr(lst1))

if lst1 == reversestr(lst1):
    print("input string is a Pallendrom")
else:
    print("input string is not pallendrom")