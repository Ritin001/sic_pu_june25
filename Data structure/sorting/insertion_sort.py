def insertion_sort(arr,last_index):
    if last_index <= 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    insertion_sort(arr, last_index - 1)
    for i in range(1, last_index + 1):
        for j in range(i, -1, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr


example_list = [3, 6, 8, 10, 1, 2, 1]
print("Original list:", example_list)
insertion_sort(example_list, len(example_list) - 1)
print("Sorted list:", example_list)