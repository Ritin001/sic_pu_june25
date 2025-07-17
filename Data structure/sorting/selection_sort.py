given_list = list(map(int, input("Enter the numbers separated by space: ").split()))
for i in range(len(given_list)):
    min_number_index = i
    for j in range(i+1,len(given_list)):
        if given_list[j] < given_list[min_number_index]:
            min_number_index = j
    if min_number_index != i:
        given_list[i], given_list[min_number_index] = given_list[min_number_index], given_list[i]
print("Sorted list:", given_list)