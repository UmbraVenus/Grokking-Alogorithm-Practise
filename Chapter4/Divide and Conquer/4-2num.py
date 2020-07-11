def countNum(listA):
    if not listA:
        return 0
    else:
        return 1 + countNum(listA[1:])

listB = [1, 2, 2, 4, 5, 6,7]
print(countNum(listB))