#uses a loop that iterates through all the elements to check the existence of the target element

#using loops and in
test_list = [1,6,3,5,3,4]
print("checking if 4 exists in list (using loop):")
for i in test_list:
    if(i == 10):
        print("Element Exists")
print("checking if 4 exits in list (using in):")
if (10 in test_list):
    print("Element Exits")
else:
    print("Element doesnt exists")
