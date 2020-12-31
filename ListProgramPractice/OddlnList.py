# Python program to print Even Numbers in a List
# list1 = [10,21,4,45,66,93]
# for num in list1:
#     if num % 2 != 0:
#         print("odd number",num,end = " ")
#     else:
#         print("even number",num)
#################################################
#using input list
# n = int(input("enter number of elements for list2"))
# list2=[]
# for i in range(n):
#     maxvalue = int(input("enter list2 values"))
#     list2.append(maxvalue)
# print(list2)
# for num1 in list2:
#     if num1 % 2 != 0:
#         print("odd number",num1,end = " ")
#     else:
#         print("even number",num1)

###################################################
#using function
# def myEven(list3):
#     for num2 in list3:
#         if num2 % 2 != 0:
#             print("odd number",num2,end = " ")
#         else:
#             print("even number",num2)
#     return num2
# m = int(input("enter number of elements for list3"))
# list3=[]
# for i in range(m):
#     maxvalue = int(input("enter list3 values"))
#     list3.append(maxvalue)
# print(list3)
# print("Odd Number",myEven(list3),end= " ")
#######################################################
#using whileloop:
list4 = [10,21,4,45,66,93]
num3 = 0
while(num3 < len(list4)):
    if num3 % 2 != 0:
        print("Odd number in list",list4[num3],end=" ")
    num3 += 1
print("\n Given list",list4)