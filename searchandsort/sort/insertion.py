def insertionSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        pos = index
        while pos > 0 and currentvalue < alist[pos - 1]:
            alist[pos] = alist[pos - 1]
            pos -= 1
        alist[pos] = currentvalue


alist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
insertionSort(alist)
print(alist)
