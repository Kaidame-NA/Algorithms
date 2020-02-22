def partition(array, start, end):
    pivotval = array[end - 1]
    leftBound = start - 1
    for i in range(start, end-1):
        if array[i] < pivotval:
            leftBound += 1
            (array[i], array[leftBound]) = (array[leftBound], array[i])
    (array[end-1], array[leftBound+1]) = (array[leftBound+1], array[end-1])
    return array


def quicksort(array, start, end):
    return array


print(partition([2, 8, 7, 1, 3, 5, 6, 4], 0, 8))
