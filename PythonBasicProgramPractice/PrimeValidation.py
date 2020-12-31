# A optimized school method based
# Python3 program to check
# if a number is prime

def isPrime(n):
    #corner case
    if (n <= 1):
        return False
    if(n <= 3):
        return True
    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while(i*i<=n):
        if (n % i == 0 or n %(i+2)==0):
            return False
        i=i+6
        return True

#Driver Program
num=int(input('Enter number to validate'))
if(isPrime(num)):
    print("Given Number is Prime")
else:
    print("Given Number is not a Prime")

