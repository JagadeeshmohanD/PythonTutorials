# Python program to find smallest number in a list
list1 = [20,10,20,4,100,10]
list1.sort()
print(list1)
print("smallest element is:",*list1[:1])
###################################################
#using min()
n = int(input("enter number of elements for list2"))
list2=[]
for i in range(n):
    minvalue = int(input("enter list2 values"))
    list2.append(minvalue)
print(list2)
print("smallest element is:",min(list2))
#######################################################
