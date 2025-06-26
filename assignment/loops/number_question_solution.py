#biggest digit in a number
dig=input("Enter a number for getting the largest digit: ")
biggest=0
for i in dig:
    if int(i)>biggest:
        biggest=int(i)
print("The biggest digit in the number is:", biggest)




#2nd smallest digit in a number
dig=input("Enter a number for getting the 2nd largest digit: ")
list1=[]
for i in dig:
        list1.append(int(i))
list1=set(list1)  
list1=list(list1)  
list1.sort()
print(list1[1]) 



#number of prime digits in a number
count=0
dig=input("Enter a number to count the number of prime digits: ")
for i in dig:
    if int(i) in [2, 3, 5, 7]:
        count+=1
print("The number of prime digits in the number is:", count)




#prime number in decreasing order
st,end=input("Enter the start and end of the range for prime numbers in decreasing order: ").split()
st = int(st)
end = int(end)
for i in range(end, st-1, -1):
     count_prime=0
     for j in range(2, i):
         if i%j==0:
             count_prime+=1
     if count_prime==0 and i>1:
        print(i, end=' ')




#fibonacci series
n = int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 1, 2
print("Fibonacci series:")
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b



#sum of series
n,m=input("enter the number and number of terms in the series: ").split()
n= int(n)
m= int(m)
den=1
sum=0
for i in range(m):
    pow=2**i
    sign=(-1)**i
    num=sign*(n**pow)/den
    sum=sum+num
    den=den+2
print(sum)

