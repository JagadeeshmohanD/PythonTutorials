# Python program to find smallest number in a list
list1 = [20,10,20,4,100,10]
list1.sort()
print(list1)
print("largest element is:",list1[-1])
###################################################
#using max()
n = int(input("enter number of elements for list2"))
list2=[]
for i in range(n):
    maxvalue = int(input("enter list2 values"))
    list2.append(maxvalue)
print(list2)
print("largest element is:",max(list2))
#######################################################
#function def myMax()

def myMax(list3):
    max = list3[0]
    for x in list3:
        if x > max :
            max = x
    return max
#driver code
m = int(input("enter number of elements for list3"))
list3=[]
for i in range(m):
    maxvalue = int(input("enter list3 values"))
    list3.append(maxvalue)
print(list3)
print("largest element is:",myMax(list3))