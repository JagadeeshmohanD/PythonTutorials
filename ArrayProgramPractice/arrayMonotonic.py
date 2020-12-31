#An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
def isMonotonic(A):
    return (all(A[i]<=A[i+1]for i in range(len(A)-1)) or
            all(A[i]>=A[i+1]for i in range(len(A)-1)))
#driving program
# A = [6,5,4,4]
A=[5,4,7,9,3]
if bool(True):{
    print(isMonotonic(A),"monotonic")
}
else:{
    print("not monotonic")
}