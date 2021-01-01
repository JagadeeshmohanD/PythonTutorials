# Python3 code to demonstrate  Sum of number digits in List using loop + str()
def sumlistloop(test_list):
    res = []
    for ele in test_list:
        sum = 0
        for digit in str(ele):
            sum += int(digit)
        res.append(sum)
    return res[:]

#drive code
n = int(input("enter number of elements for lists"))
test_list=[]
for i in range(n):
    list1 = int(input("enter lists values"))
    test_list.append(list1)
print("The Original given list",test_list)
print("List The sum of cumulative list",sumlistloop(test_list))
