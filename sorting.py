def quick_sort(arr, low, high, compare_func):
    if low < high:
        pi = partition(arr, low, high, compare_func)
        quick_sort(arr, low, pi - 1, compare_func)
        quick_sort(arr, pi + 1, high, compare_func)


def partition(arr, low, high, compare_func):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if compare_func(arr[j], pivot) <= 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1