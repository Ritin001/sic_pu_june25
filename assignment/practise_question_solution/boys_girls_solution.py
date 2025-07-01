total_students = int(input("Enter the total number of students: "))
boys_height = list(map(int, input("Enter the heights of boys: ").split()))
boys_height.sort()
girls_height = list(map(int, input("Enter the heights of girls: ").split()))
girls_height.sort()
ideal_line=[]
ideal_line_2=[]
for i in range(total_students):
    ideal_line.append(boys_height[i])
    ideal_line.append(girls_height[i])
for i in range(total_students):
    ideal_line_2.append(girls_height[i])
    ideal_line_2.append(boys_height[i])
boys_height.extend(girls_height)
boys_girls_height=boys_height.copy()

boys_girls_height.sort()
if ideal_line == boys_girls_height or ideal_line_2 == boys_girls_height:
    print("YES")
else:   
    print("NO") 





