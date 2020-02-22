def partition(array, start, end):
    pivot_value = array[end]
    left_bound = start - 1
    for i in range(start, end):
        if array[i] < pivot_value:
            left_bound += 1
            (array[i], array[left_bound]) = (array[left_bound], array[i])
    (array[end], array[left_bound + 1]) = (array[left_bound + 1], array[end])
    return left_bound + 1


def quick_sort(array, start=0, end=None):
    if end is not None:
        if start < end:
            pivot = partition(array, start, end)
            quick_sort(array, start, pivot - 1)
            quick_sort(array, pivot + 1, end)
    else:
        pivot = partition(array, start, len(array) - 1)
        quick_sort(array, start, pivot - 1)
        quick_sort(array, pivot + 1, len(array) - 1)

    return array


print(quick_sort([3, 4, 5, 1, 2, 1, 1, 1, 1, 13],5))
