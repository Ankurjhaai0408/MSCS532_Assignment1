def insertion_sort_desc(arr):
    for i, current in enumerate(arr[1:], start=1):
        j = i - 1
        while j >= 0 and arr[j] < current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr

# Example usage
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Sorted in Descending Order:", insertion_sort_desc(data))

