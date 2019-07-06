def merge_sort(alist):
    print('Splitting: ', alist)
    if len(alist) > 1:
        mid len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i +=1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i +=1
            k +=1
        while j < len(righthalf):
            alist[k] = lefthalf[j]
            j +=1
            k +=1
    print("merging: ", alist)

alist = [34, 12,1, 3, 52, 23, 83, 72, 37, 93, 57, 44, 25]
mergeSort(alist)
