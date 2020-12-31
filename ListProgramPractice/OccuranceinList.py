# # Python code to count the number of occurrences
# def countx(li1,x):
#     count = 0
#     for ele in li1:
#         if (ele == x):
#             count = count + 1
#     return count
#
# #driving code
# m = int(input("enter number of elements for li1"))
# li1=[]
# for i in range(m):
#     loccur = int(input("enter list1 values"))
#     li1.append(loccur)
# print("the entered list elements are",li1)
# x = int(input("enter element to find occurance in list"))
# print('{} has occurred {} times'.format(x, countx(li1, x)))

#############################################################
def count1y(li2, y):
    return li2.count(y)
#driving code
n = int(input("enter number of elements for li1"))
li2=[]
for i in range(n):
    loccur = int(input("enter list1 values"))
    li2.append(loccur)
print("the entered list elements are",li2)
y = int(input("enter element to find occurance in list"))
print('{} has occurred {} times'.format(y, count1y(li2, y)))
