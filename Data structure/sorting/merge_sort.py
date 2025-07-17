def merge_sort(arr):
   
    # Base case: If the list has 0 or 1 element, it's already sorted.
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the list into two halves.
    # Find the middle index of the list.
    mid = len(arr) // 2
    # Recursively sort the left half.
    left_half = merge_sort(arr[:mid]) # Recursive call for left sub-array
    # Recursively sort the right half.
    right_half = merge_sort(arr[mid:]) # Recursive call for right sub-array

    # Step 2: Conquer (Merge) the sorted halves.
    # Initialize pointers for the left_half, right_half, and the merged result.
    i = j = k = 0
    merged_arr = [] # Initialize an empty list to store the merged result

    # Compare elements from left_half and right_half and merge them
    # into merged_arr in sorted order.
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged_arr.append(left_half[i])
            i += 1
        else:
            merged_arr.append(right_half[j])
            j += 1

    # Add any remaining elements from the left_half (if any).
    while i < len(left_half):
        merged_arr.append(left_half[i])
        i += 1

    # Add any remaining elements from the right_half (if any).
    while j < len(right_half):
        merged_arr.append(right_half[j])
        j += 1

    return merged_arr

# --- Example Usage ---
if __name__ == "__main__":
    # Single Test Case: Unsorted list
    unsorted_list = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original list: {unsorted_list}")
    sorted_list = merge_sort(unsorted_list)
    print(f"Sorted list: {sorted_list}\n")