#sum of series 13 + 23 + 33 + 43 + …….+ n3 till n
#(n ( n + 1 ) / 2) ^ 2

def sumOfSeriesCube(n):
    sum1 = 0
    for i in range(1, n+1):
        sum1+=i*i*i
    return sum1

#driver function
n=int(input("Enter number for which sum of cube series "))
print(sumOfSeriesCube(n))