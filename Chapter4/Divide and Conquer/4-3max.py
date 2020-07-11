def maxNum(listA):
    if not listA:
        return 0
    else:
        num = listA[0]
        if not listA[1:]:
            return num
        elif maxNum(listA[1:]) > num:
            return maxNum(listA[1:])
        else:
            return num

listB = [201, 2, 3, 89, 189]
print(maxNum(listB))
        