# Python program to multiply all values in the list using traversal
import numpy
import math
def multiplList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

#driver code
list1 = [1,2,3]
list2 = [3,2,4]
print(multiplList(list1))
print(multiplList(list2))
###############################################################
list3 = [7,8,9]
list4 = [1,5,9]
result1 = numpy.prod(list3)
result2 = numpy.prod(list4)
print("The product of result1",result1)
print("The product of result2",result2)
##################################################################
n = int(input("enter number of elements for list5"))
list5=[]
for i in range(n):
    prod1 = int(input("enter list5 values"))
    list5.append(prod1)
print(list5)
result3 = math.prod(list5)
print(result3)
