# Program to multiply two matrices using nested loops take a 3x3 matrix
#take a 3*3 matrix
a=[[12,7,3],
   [4,5,6],
   [7,8,9]]
#take a 3*4 matrix
b=[[5,8,1,2],
   [6,7,3,0],
   [4,5,9,1]]
#result will be 3*4
result=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

#iteating by row of A
for i in range(len(a)):
    #iterating by coloum by b
    for j in range(len(b[0])):
        #iterating rows of b
        for k in range(len(b)):
            result[i][j]+=a[i][k]*b[k][j]

for r in result:
    print(r)

###########################################################
# Program to multiply two matrices (vectorized implementation)
import numpy as np
#take a 3*3 matrix
a1=[[12,7,3],
   [4,5,6],
   [7,8,9]]
#take a 3*4 matrix
b1=[[5,8,1,2],
   [6,7,3,0],
   [4,5,9,1]]
#result will be 3*4
result1=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
result1 = np.dot(a1,b1)
for r1 in result1:
    print(r1)

