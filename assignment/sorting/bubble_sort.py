given_list = list(map(int, input("Enter the numbers separated by space: ").split()))
for i in range(len(given_list) - 1):
    for j in range(len(given_list) - 1 - i):
        if given_list[j] > given_list[j + 1]:
            given_list[j], given_list[j + 1] = given_list[j + 1], given_list[j]
print("Sorted list:", given_list)
