from collections import OrderedDict
def removedupwithoutorder(str1):
    return "".join(set(str1))

def removedupwithorder(str1):
    return "".join(OrderedDict.fromkeys(str1))

if __name__ == "__main__":
    str1 = input("Enter string for duplicate validation")
    print("Duplicate string with out order:",removedupwithoutorder(str1))
    print("Duplicate string with order :",removedupwithorder(str1))
###############################################
from collections import OrderedDict
seq = ('name','age','gender')
dict = OrderedDict.fromkeys(seq)

print(str(dict))
dict = OrderedDict.fromkeys(seq, 10)

print(str(dict))