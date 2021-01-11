# Python3 code to demonstrate working of  Words Frequency in String Shorthands Using dictionary comprehension + count() + split()
def freq(test_str):
    res = {key: test_str.count(key) for key in test_str.split()}
    print("The words frequency :" + str(res))

#driving program
test_str = input("Enter the string ")
print("Given string :"+ test_str)
freq(test_str)
##########################################

from collections import Counter
res1 = Counter(test_str.split())
print("The words frequency :" + str(dict(res1)))
