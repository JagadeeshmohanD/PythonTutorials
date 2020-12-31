#Sum of squares of first n natural numbers
#Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2
#sum of square of first N natural number = (n*(n+1)*(2*n+1))/6
def squaresum(n):
    return (n*(n+1)*(2*n+1))//6

n=int(input("Enter the number to find squaresum"))
print(squaresum(n))