given_list=list(map(int, input("Enter the list of numbers separated by space: ").split()))
search_element = int(input("Enter the number to search: "))
result = False
for i in given_list:
    if i == search_element:
        result = True
        break
if result:
    print(f"{search_element} is present in the list.")
else:
    print(f"{search_element} is not present in the list.")