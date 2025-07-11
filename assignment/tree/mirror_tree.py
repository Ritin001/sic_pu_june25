n= int(input("enter the number od nodes"))
left_first= list(map(str,input().split()))
right_first= list(map(str,input().split()))
right_second= list(map(str,input().split()))
left_second= list(map(str,input().split()))

if left_first[0:len(left_first)-1] == right_second[0:len(right_second)-1] and right_first[0:len(right_first)-1] == left_second[0:len(left_second)-1]:
    print("yes")
else:
    print("no") 