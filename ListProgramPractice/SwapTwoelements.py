def swapPosition(list,pos1,pos2):
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list

list = [23,65,19,20,50,40]
pos1,pos2 = 1,3

print(swapPosition(list,pos1-1,pos2-1))

#using tuple variable get
def swapPositiontuple(list1,post1,post2):
    get = list1[post1],list1[post2]
    list1[post2],list1[post1] = get
    return list1
list1 = [23,65,19,90,52]
post1,post2 = 1,3
print(swapPositiontuple(list1,post1-1,post2-1))