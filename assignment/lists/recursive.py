# factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
number=5
print("Factorial of", number, "is:", factorial(number))


# Fibonacci series using recursion
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series
fibonnaci_number = 10
print("Fibonacci series up to", fibonnaci_number, "is:", fibonacci(fibonnaci_number))


#sum of number in a list using recursion
def sum_of_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_of_list(lst[1:])
list_numbers = [1, 2, 3, 4, 5]
print("Sum of numbers in the list is:", sum_of_list(list_numbers))