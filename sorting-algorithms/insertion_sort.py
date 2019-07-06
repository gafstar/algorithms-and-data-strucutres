def insertion_sort(alist):
    for i in range(1, len(alist)):

        currentValue = alist[i]
        position = i

        while position > 0 and alist[position - 1] > currentValue:
            alist[position] = alist[position - 1] 
            position = position -1
            # The above two lines can be re-written as 
            # alist[position], position = alist [position-1], position-1

        alist[position] = currentValue
    return alist

    alist = [34, 12,1, 3, 52, 23, 83, 72, 37, 93, 57, 44, 25]
    insertion_sort(alist)