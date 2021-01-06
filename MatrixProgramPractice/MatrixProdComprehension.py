# Python3 code to demonstrate Matrix Product Using list comprehension + loop
#getting product
def prod(val):
    res = 1
    for ele in val:
        res*=ele
    return res

# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
# driver code
# n = int(input("enter number of elements for list1"))
# test_list=[]
# for i in range(n):
#     list1 = tuple(input("enter list1 string values"))
#     test_list.append(list1)
print("The original list:"+str(test_list))
# using list comprehension + loop Matrix Product
res = prod([ele for sub in test_list for ele in sub])
#print result
print("The total element product in list is:"+str(res))