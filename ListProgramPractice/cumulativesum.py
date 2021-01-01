# Python code to get the Cumulative sum of a list
# def cumulative(lists):
#     cu_list = []
#     length = len(lists)
#     cu_list =[sum(lists[0:x:1]) for x in range(0, length+1)]
#     return cu_list[1:]
#
# #drive code
# n = int(input("enter number of elements for lists"))
# lists=[]
# for i in range(n):
#     lists1 = int(input("enter lists values"))
#     lists.append(lists1)
# print(lists)
# print("The sum of cumulative list",cumulative(lists))
##############################################################
def cumsum(list1):
    new_list=[]
    j=0
    for i in range(0,len(list1)):
        j+=list1[i]
        new_list.append(j)
    return new_list[1:]

#drive code
m = int(input("enter number of elements for lists"))
listcu=[]
for k in range(m):
    list1 = int(input("enter lists values"))
    listcu.append(list1)
print(list1)
print("The sum of cumulative list",cumsum(listcu))
