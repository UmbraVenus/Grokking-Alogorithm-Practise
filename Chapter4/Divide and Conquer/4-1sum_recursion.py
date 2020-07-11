def sum_recursion(listB):
    if not listB:
        return 0
    else:
        return listB[0] + sum_recursion(listB[1:])

listA = [1, 2, 3, 4, 5, 6]
print(sum_recursion(listA))