# list1 = [-10,21,-4,-45,-66,93,0,96,00,-8]
# num = 0
# while(num <len(list1)):
#     if list1[num] > 0:
#         print("Postive Number",list1[num],end = " ")
#         num += 1
#     elif list1[num] < 0:
#         print("Negative Number",list1[num],end= " ")
#         num += 1
#     else:
#         print("Number is Zero",list1[num],end=" ")
#         num += 1
#
##############################################################
def posNeg(list2):
    num1 = 0
    while (num1 < len(list2)):
        if list2[num1] > 0:
            print("Postive Number", list2[num1], end=" ")
            num1 += 1
        elif list2[num1] < 0:
            print("Negative Number", list2[num1], end=" ")
            num1 += 1
        else:
            print("Number is Zero", list2[num1], end=" ")
            num1 += 1
    return list2

#driver code
m = int(input("enter number of elements for list2"))
list2=[]
for i in range(m):
    value = int(input("enter list1 values"))
    list2.append(value)
print(list2)
print("posneg number is:",posNeg(list2))
