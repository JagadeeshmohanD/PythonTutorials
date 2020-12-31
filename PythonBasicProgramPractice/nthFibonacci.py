#creating an array in the function to find the nth number in fibonacci series. [0,1,1,...]
def fibonaccci(n):
    arr = [0]*(n+1)
    arr[1]=1
    for i in range(2,n+1):
        arr[i] = arr[i-1]+arr[i-2]
    return arr[n]

#driver program
if __name__ == "__main__":
    print(fibonaccci(int(input("Enter the term :"))))
# lets assume the input as 12

