# Heap Sort Implementation
# i is a subtree index and n is size or heap

def heapify(arr, n, i):
    largest = i         # initialize largest as root
    l = 2 * i +1        # left = 2*i +1
    r = 2 * i +2        # right = 2*i +2

    # see if the left child of root exists an is greater than root
    if r < n and arr[i] < arr[l]:
        largest = l

    # see if right child of root exists and is greater than root
    if r < n and arr[i] < arr[r]
        largest = r

    # change root if needed
    if largest !=i:
        arr[i], arr[largest] = arr[largest], arr[i]  #swap

        # Heapify the root
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heap_sort(arr):
    n = len(arr)

    # build a maxheap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # one by one extract elements
    for i in range (n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)

# Driver code to test above

arr = [12, 11, 13,5, 6, 7]
heap_sort(arr)
print ('Sorted array is: ')
for i in range(n):
    print ('%d', %arr[i])
