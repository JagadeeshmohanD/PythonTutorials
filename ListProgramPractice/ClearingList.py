# Python3 code to demonstrate  clearing a list using clear and Reinitializing

list1 = [1,2,3]
list2 = [5,6,7]
print("List1 before deleting is :"+ str(list1))
list1.clear()
print("list1 after deleting is :"+str(list1))
print("list2 before deleting is :"+str(list2))
list2.clear()
print("list after deleting is :"+str(list2))

#using delete operation
list3 = [8,9,10]
print("list3 before deleting is :"+str(list3))
del list3[:]
print("list3 after deleting is "+str(list3))
