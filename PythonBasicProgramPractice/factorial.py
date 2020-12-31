def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)

#driver code
num = int(input("Enter First Number to find factorial:"))
print("Factorial of",num,"is",factorial(num))
