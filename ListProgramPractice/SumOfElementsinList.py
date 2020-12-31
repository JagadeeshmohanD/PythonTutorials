# Python program to find sum of elements in list
total = 0
ele = 0
list1 = [11,5,17,18,23]
# Iterate each element in list and add them in variale total
while(ele < len(list1)):
    total = total+list1[ele]
    ele += 1
print("sum of all elements in given list:",total)

###########################################################
n = int(input("number of elements in list"))
list2=[]
for i in range(n):
    elem = int(input("enter list values"))
    list2.append(elem)
print(list2)
total1 = sum(list2)
print("sum of all elements in given list:",total1)
