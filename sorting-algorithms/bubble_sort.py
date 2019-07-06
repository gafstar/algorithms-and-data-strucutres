def bubbleSort(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j]>alist[j+1]:
                temp = alist[j]
                alist[j] = alist [j+1]
                alist[j+1] = temp
    return alist
        
alist = [34, 12,1, 3, 52, 23, 83, 72, 37, 93, 57, 44, 25]
bubbleSort(alist)


# or 
def bubbleSort(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j]>alist[j+1]:
                temp = alist[j]
                alist[j] = alist [j+1]
                alist[j+1] = temp
    return alist
        
alist = [34, 12,1, 3, 52, 23, 83, 72, 37, 93, 57, 44, 25]
bubbleSort(alist)