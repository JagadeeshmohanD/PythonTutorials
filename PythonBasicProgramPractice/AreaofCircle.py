# area = pi*r*r
def findArea(r):
    pI=3.142
    return pI*(r*r)

#driver method
r = float(input('Enter Radius of circle'))
print("Area is %.6f" % findArea(r))
