# Program to add two matrices using nested loop
x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
y=[[9,8,7],
   [6,5,4],
   [3,2,1]]
result =[[0,0,0],
         [0,0,0],
         [0,0,0]]
# iterate through rows
for i in range(len(x)):
    # iterate through columns
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]

for r in result:
    print(r)

##########################################################
# Program to add two matrices using list comprehension
p=[[1,2,3],
   [4,5,6],
   [7,8,9]]
q=[[9,8,7],
   [6,5,4],
   [3,2,1]]
result1 = [[x[i][j]+y[i][j] for  j in range(len(x[0]))] for  i in range(len(x))]
for r in result:
    print(result1)