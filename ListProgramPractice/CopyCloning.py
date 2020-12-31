# Python program to copy or clone a list Using the Slice Operator
def cloning(li1):
    li1_copy = li1[:]
    return li1_copy

#driving code
m = int(input("enter number of elements for li1"))
li1=[]
for i in range(m):
    lvalur = int(input("enter list3 values"))
    li1.append(lvalur)
print("the entered li are",li1)
li1.sort()
print(li1)
li2=cloning(li1)
print("after cloning",li2)