given_list=list(map(int, input("Enter the sorted list of numbers separated by space: ").split()))
search_element = int(input("Enter the number to search: "))
start=0
end=len(given_list)-1
result = False
location = -1
while start <= end:
    mid = (start + end) // 2
    if given_list[mid] == search_element:
        result = True
        location = mid+1
        break
    elif given_list[mid] < search_element:
        start = mid + 1
    else:
        end = mid - 1
if result:
    print(f"{search_element} is present in the list. Location: {location}")
else:
    print(f"{search_element} is not present in the list.")