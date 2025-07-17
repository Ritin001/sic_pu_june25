'''orange = int(input("enter the number of oranges"))
orange_size_number=list(map(int,input("enter the size of oranges separated by space").split()))
orange_in_hand=[orange_size_number[orange-1]]
#orange_size_number=orange_size_number[1:len(orange_size_number)-1]
orange_children=[]
orange_sell=[]
for i in orange_size_number:
    if i > orange_in_hand[0]:
        orange_sell.append(i)
    elif i < orange_in_hand[0]:
        orange_children.append(i)
result = orange_children + orange_in_hand + orange_sell
print("The final arrangement of oranges is:", result)'''



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