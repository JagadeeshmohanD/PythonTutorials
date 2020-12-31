list1 = [11, 5, 17, 18, 23, 50,[],8,[],0]
list2 =[]
list3 =[]
list4 =[]
list5 =[]
for ele in list1:
    if ele % 2 == 0:
        list2.append(ele)
        list1.remove(ele)
    elif ele % 2 != 0:
        list3.append(ele)
    elif ele == []:
        list4.append(ele)
    else:
        list5.append(ele)

print("new list after removing all even number: ",list1)
print("even number list:",list2)
print("odd number in list",list3)
print("zero in the given list",list4)
print("empty list",list5)