def Remove(tuples):
    tuples = [t for t in tuples if t]
    # tuples = filter(None, tuples)
    return tuples

#driver code
tuples = [(),('ram','15','$#@'),(),('laxman','sita'),('krishna','akbar','45'),('',''),()]
# n = int(input("enter number of elements for tuple"))
# tuples=[]
# for i in range(n):
#     loccur = tuple(input("enter tuples values"))
#     tuples.append(loccur)
print("given tuples",tuples)
print("empty removed tuple", Remove(tuples))
