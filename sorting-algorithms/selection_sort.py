def selectionSort(alist):
  for i in range(len(alist)-1, 0, -1):
    maxPosition = 0
    for j in range(1, i+1):
      if alist[j] > alist[maxPosition]:
          maxPosition = j
    
      temp = alist[i]
      alist[i] = alist[maxPosition]
      alist[maxPosition] = temp
    
  return alist

alist = [34, 12,1, 3, 52, 23, 83, 72, 37, 93, 57, 44, 25]
selectionSort(alist)

# or

def selectionSort(alist):
  for i in range(len(alist)-1, 0, -1):
    maxPosition = 0
    for j in range(1, i+1):
      if alist[j] > alist[maxPosition]:
          maxPosition = j
      alist[i], alist[maxPosition] = alist[maxPosition], alist[i]
        
  return alist

alist = [34, 12,1, 3, 52, 23, 83, 72, 37, 93, 57, 44, 25]
selectionSort(alist)