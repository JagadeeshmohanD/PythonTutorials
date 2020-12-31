list1 = [11, 5, 17, 18, 23, 50,[],8,[],0]
list2 =[]
list3 =[]
for num in list1:
    if num == []:
        list2.append(num)
    else:
        list3.append(num)
print("given list",list1)
print("empty list",list2)
print("list after modification",list3)