def quick_sort(arr,pivot_index, end_index):
    if pivot_index < end_index:
        partition_index = partition(arr, pivot_index, end_index)
        quick_sort(arr, pivot_index, partition_index - 1)
        quick_sort(arr, partition_index + 1, end_index)
def partition(arr, pivot_index, end_index):
    pivot = arr[end_index]
    i = pivot_index - 1
    for j in range(pivot_index, end_index):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end_index] = arr[end_index], arr[i + 1]
    return i + 1
#example usage
example_list = [3, 6, 8, 10, 1, 2, 1]
print("Original list:", example_list)

quick_sort(example_list, 0, len(example_list) - 1)        
print("Sorted list:", example_list)