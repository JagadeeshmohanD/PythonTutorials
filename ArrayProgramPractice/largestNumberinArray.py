def lagest(arr,n):
    max = arr[0]
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    return max

#drive code
arr =[10,11,10,42,74,21]
n=len(arr)
ans=lagest(arr,n)
print("largest in given array is",ans)