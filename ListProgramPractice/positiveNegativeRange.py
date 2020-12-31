start = int(input("Enter start Range"))
end = int(input("Enter end Range"))
listpo = []
listne = []
for num in range(start,end +1):
    if num > 0:
        # print("Postive Number", num, end=" ")
        listpo.append(num)
        num += 1
    elif num < 0:
        # print("Negative Number", num, end=" ")
        listne.append(num)
        num += 1
    else:
        print("Number is Zero", num, end=" ")
        num += 1

print(listpo)
print(listne)
print("number Range",start,end)