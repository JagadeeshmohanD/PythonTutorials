#A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square
import math
i=0
list1=[]
list2=[]
def ifperfectSquare(x):
    s=int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perferct square
    return ifperfectSquare(5*n*n+4) or ifperfectSquare(5*n*n-4)

# A utility function to test above functions
def range(x,y):
    for i in range(x,y):
        if (isFibonacci(i) == True):
            print (i,"is a Fibonacci Number")
            list1.append(i)
        else:
            print(i,"is not a Fibonacci Number")
            list2.append(i)
        return (list1,list2)

#driving code
x=int(input("enter range x"))
y=int(input("enter range y"))
print(list1)
print(list2)
