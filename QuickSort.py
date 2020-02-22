def partition(array, start, end):
    pivot_value = array[end]
    left_bound = start - 1
    for i in range(start, end):
        if array[i] < pivot_value:
            left_bound += 1
            (array[i], array[left_bound]) = (array[left_bound], array[i])
    (array[end], array[left_bound + 1]) = (array[left_bound + 1], array[end])
    return left_bound + 1


def quick_sort(array, start=0, end=-1):
    if end == -1:
        end = len(array) - 1
    if start == end:
        return
    pivot = partition(array, start, end)
    quick_sort(array, start, pivot - 1)
    quick_sort(array, pivot + 1, end)
    return array


print(quick_sort([3, 4, 5, 1, 2], 0, 4))
