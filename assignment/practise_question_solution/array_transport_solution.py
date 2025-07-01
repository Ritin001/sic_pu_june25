len_main_list=int(input("Enter the length of the main list: "))
main_list=list(map(int, input("Enter the elements of the main list: ").split()))
len_second_list=int(input("Enter the length of the second list: "))
second_list=list(map(int, input("Enter the elements of the second list: ").split()))
for i in second_list:
    if i in main_list:
        main_list.remove(i)
print("The main list after removing elements from the second list is:", set(main_list))