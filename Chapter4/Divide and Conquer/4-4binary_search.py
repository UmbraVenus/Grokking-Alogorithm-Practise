def binarySearch(a, A):
    if not A:
        return "Uh oh :("
    else:
        lower = 0
        upper = len(A)
        mid = (lower + upper) // 2
        print(A)
        if a == A[mid]:
            return "bingo!"
        elif a > A[mid]:
            return binarySearch(a, A[mid + 1: upper])
        else:
            return binarySearch(a, A[lower:mid])

B = [1, 2, 4, 5, 6, 99, 200]
print(binarySearch(99, B))
# This exercise calls for whether or not the elem is in the array,
# not to point out the index of elem