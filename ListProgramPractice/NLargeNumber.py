# Python program to find N largest element from given list of integers
n = int(input("enter number of elements for list1"))
list1=[]
for i in range(n):
    maxvalue = int(input("enter list2 values"))
    list1.append(maxvalue)
print(list1)
list1.sort()
print(list1)
Nl=int(input("enter N largest number to find"))
print("N largest element is:",list1[-Nl:])
################################################################
def myMax(list2):
    max = list2[0]
    for x in list2:
        if x > max :
            max = x
    return max
#driver code
m = int(input("enter number of elements for list2"))
list2=[]
for i in range(m):
    maxvalue = int(input("enter list3 values"))
    list2.append(maxvalue)
print(list2)
list2.sort()
print(list2)
Nlf=int(input("enter N largest number to find"))
print("N largest element is:",list2[-Nlf:])
