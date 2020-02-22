def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
        merge_sort(left)
        merge_sort(right)

        i = j = 0

        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                array[i + j] = left[i]
                i += 1
            else:
                array[i + j] = right[j]
                j += 1
        while len(left) > i:
            array[i + j] = left[i]
            i += 1

        while len(right) > j:
            array[i + j] = right[j]
            j += 1

    return array


print(merge_sort([2, 3, 1, 1, 1, 13, 12, 12, 1, 200, 1, 1]))
