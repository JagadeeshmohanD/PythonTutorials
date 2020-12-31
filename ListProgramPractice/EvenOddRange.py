start = int(input("Enter start Range"))
end = int(input("Enter end Range"))
for num in range(start,end +1):
    if num % 2 == 0:
        print("Even Number",num,end = " ")
    else:
        print("Odd Number",num)
print("number Range",start,end)