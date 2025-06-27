num=int(input("Enter a number to print the pattern: "))

#right angles triangle
for i in range(num):
    print("*" * (i + 1))
print()
print()




#equilateral triangle
for i in range(num):
    print(" " * (num - i - 1) + "*" * (2 * i + 1))


print()
print()





#hollow square
for i in range(num):
    for j in range(num):
        if i == 0 or i == num - 1 or j == 0 or j == num - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
print()
print()





#hollow rhombus
for i in range(num-1,-1,-1):
    print(" " * i ,end="")
    for j in range(num):
        if i == 0 or i == num - 1 or j == 0 or j == num - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


print()
print()




#pascal triangle
num=num-1
temp_list=[]
temp_list2=[]
print("  "*(num+1) + "  1")
for i in range(num):
    temp_list2=[]
    print("  "* (num-i),end="")
    print("  1","",end="")
    temp_list2.append(1)
    for j in temp_list:
        print(f"{j:3d}", end=" ")
        temp_list2.append(j)
    print("  1","",end="")
    temp_list2.append(1)
    temp_list=[]
    r1=(len(temp_list2))-1
    for j in range (r1):
        temp_num=temp_list2[j] + temp_list2[j+1]
        temp_list.append(temp_num)
        temp_num=0
    print()
print()
print()   

    
num=num+1

#x shape
for i in range(num):
    for j in range(num):
        if i == j or  i + j == num - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()
print()






#x shape inside hollow square
for i in range(num):
    for j in range(num):
        if i == j or  i + j == num - 1 or i == 0 or i == num - 1 or j == 0 or j == num - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()
print()



#benzene ring
n=7
n2=n//2# for half part
# first half part
for i in range(0,n2+1):
    for j in range(0,n):
        if j>=n2-i and j<n-n2+i:
            if(j==n2-i or  j==n-n2+i-1):
                if i==0 or i==n2:
                    print("C",end="")
                elif j==n2-i:
                    print("/",end="")
                else:
                    print("\\\\",end="")
            else:
                print(" ",end="")
        else :
            print(" ",end="")
    print()
#for middle part
for i in range(n2-1):
    print("||"+" "* (n-2)+"|")
# second half part
for i in range(0,n2+1):
    for j in range(0,n):
        if j>=i and j< n-i:
            if j==i or j== n-i-1:
                if i==0 or i==n2:
                    print("C",end="")
                elif j==i :
                    print("\\",end="")
                else:
                    print("//",end="")
            else:
                print(" ",end="")
        else:
            print(" ",end="")
    print()