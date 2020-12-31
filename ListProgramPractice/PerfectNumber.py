# A number is a perfect number if is equal to sum of its proper divisors

#returns true if n is perfect
def isPerfect(n):
    # To Store sum if n is divisors
    sum =1
    # find all divisors and add them
    i = 2
    while i*i <= n:
        if n%i == 0:
            sum = sum+i+n/i
            i +=1

    #if sum of divisors is equal to n then n is a perfect number
    return (True if sum == n and n!=1 else False)

print("Below are all perfect numbers till 100")
n = 2
for n in range(100):
    if isPerfect(n):
        print(n,"is a perfect number")


