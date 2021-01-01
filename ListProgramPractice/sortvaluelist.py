#Sort the values of first list using second list in Python
# Python program to sort one list using the other list
def sort_list(list1,list2):
    zipped_pair=zip(list2,list1)
    z = [x for _, x in sorted(zipped_pair)]
    return z
# driver code
n = int(input("enter number of elements for list1"))
m = int(input("enter number of elements for list2"))
test_list1=[]
test_list2=[]
for i in range(n):
    list1 = str(input("enter list1 string values"))
    test_list1.append(list1)
for j in range(m):
    list2 = int(input("enter list2 numeric value"))
    test_list2.append(list2)
print("The Original given list1 and list2",test_list1,test_list2)
print("sorted list using the other list",sort_list(test_list1,test_list2))
