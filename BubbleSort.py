def bubblesort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])
    return array


def bubblesortwhile(array):
    comparisons = -1
    while comparisons != 0:
        comparisons = 0
        for i in range(len(array)-1):
            if array[i] > array[i + 1]:
                (array[i], array[i+1]) = (array[i+1], array[i])
                comparisons += 1
    return array


print(bubblesort([3, 4, 5, 1, 2]))
print(bubblesortwhile([3, 4, 5, 1, 2]))
