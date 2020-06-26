def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        posnOfMax = 0
        for pos in range(1, fillslot + 1):
            if alist[pos] > alist[posnOfMax]:
                posnOfMax = pos
        alist[posnOfMax], alist[fillslot] = alist[fillslot], alist[posnOfMax]


alist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
selectionSort(alist)
print(alist)
