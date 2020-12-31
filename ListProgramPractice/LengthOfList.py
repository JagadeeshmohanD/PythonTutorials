#length using len()
a = []
a.append("Hello")
a.append("Geeks")
a.append("For")
a.append("Geeks")
print("The length of list is",len(a))

#################################################
n =len([10,20,30,40,50])
print("The Length if list",n)

###################################################
# Python code to demonstrate length of list using len() and length_hint
from operator import length_hint
test_list = [1,4,5,7,8]
print("The List is:"+str(test_list))

# Finding length of list  using len()
list_len = len(test_list)

# Finding length of list  using length_hint()
list_len_hint = length_hint(test_list)


# Printing length of list
print("length if list using len() is :"+str(list_len))
print("Length of list using length_hint() is: "+str(list_len_hint))