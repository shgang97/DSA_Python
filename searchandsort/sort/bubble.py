def bubbleSort(alist):
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


alist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
bubbleSort(alist)
print(alist)
