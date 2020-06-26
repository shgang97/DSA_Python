def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        pos = i
        while pos >= gap and alist[pos - gap] > currentvalue:
            alist[pos] = alist[pos - gap]
            pos -= gap
        alist[pos] = currentvalue


def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print('After increment of size', sublistcount, 'The list is ', alist)
        sublistcount //= 2


alist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
shellSort(alist)
print(alist)
