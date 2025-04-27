def isSorted(A,n):
    if n==1 or n==0:
        print("Array is sorted")
        return True
    if A[n-1]<A[n-2]:
        print("Array is not sorted")
        return False
    return isSorted(A,n-1)
isSorted([1,1,1,1],4)

