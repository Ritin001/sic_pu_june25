#smallest and largest element in a list

list=[5,76,3,87,27,8,3,8]
list.sort()
print("Smallest element is:", list[0])  
print("Largest element is:", list[-1])

#frequenxcy of elements in a list

list_2= [2 ,5,7,5,3,5,3,5,6,2,3,5,6,7,8,9,2,3,4,5]
print("Frequency of 5 in list_2 is:", list_2.count(5))  

#remove duplicates from a list
list_3 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
list_3 = set(list_3)
print("List after removing duplicates:", list_3)

# next possible biggest number
num="45628"
num_list = []
for i in num:
    num_list.append(int(i))
for i in range(len(num_list)-1, 0, -1):
    if num_list[i] > num_list[i-1]:
        num_list[i], num_list[i-1] = num_list[i-1], num_list[i]
        break
print("Next possible biggest number is:", ''.join(map(str, num_list)))

