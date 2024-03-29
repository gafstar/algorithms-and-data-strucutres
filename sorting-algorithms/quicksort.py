def quicksort(alist):
    quicksortHelper(alist, 0, len(alist)-1)

def quicksortHelper(alist, first, last):
    if first < last:

    splitpoint= partition(alsit, first, last)
    quicksortHelper(alist, first, splitpoint -1)
    quicksortHelper(alist, splitpoint +1, last)

def partition(alsit, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <=rightmark and alist[leftmark] <=pivotvalue:
            leftmark +=1

        while alist[rightmark] >=pivotvalue and rightmark >=leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] =alist[rightmark]
            alist[rightmark]= temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

