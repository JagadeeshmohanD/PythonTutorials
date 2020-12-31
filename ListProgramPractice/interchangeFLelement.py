# Python3 program to swap first and last element of a list
#swap function
def swapList(list):
    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0,last)
    list.append(first)

    return list

#driver code
newList = [12,35,9,56,24]
print(swapList(newList))