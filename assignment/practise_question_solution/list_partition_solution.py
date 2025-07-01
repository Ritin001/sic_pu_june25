n,x,y=map((int),input().split(" "))
list=list(map(int,input().split(" ")))
list_1=list[:y]
list_2=list[y:n]
p_value_1=min(list_1)-1
p_value_2=max(list_2)+1
p_values=[]
for i in range(p_value_2,p_value_1+1):
    p_values.append(i)
print(len(p_values))