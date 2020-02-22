def partition(array, start, end):
    pivot_value = array[end]
    left_bound = start - 1
    for i in range(start, end):
        if array[i] < pivot_value:
            left_bound += 1
            (array[i], array[left_bound]) = (array[left_bound], array[i])
    (array[end], array[left_bound + 1]) = (array[left_bound + 1], array[end])
    return left_bound + 1


def quick_sort(array, start=None, end=None):
    if start is not None and end is not None:
        if start < end:
            pivot = partition(array, start, end)
            quick_sort(array, start, pivot - 1)
            quick_sort(array, pivot + 1, end)
    else:
        if start is None and end is None:
            pivot = partition(array, 0, len(array) - 1)
            quick_sort(array, 0, pivot - 1)
            quick_sort(array, pivot + 1, len(array) - 1)
        elif start is None:
            pivot = partition(array, 0, end)
            quick_sort(array, 0, pivot - 1)
            quick_sort(array, pivot + 1, end)
        else:
            pivot = partition(array, start, len(array) - 1)
            quick_sort(array, start, pivot - 1)
            quick_sort(array, pivot + 1, len(array) - 1)

    return array


print(quick_sort([3, 4, 5, 1, 2, 1, 1, 1, 1, 13],end=5))
