# Example of dictionary comprehension
n = int(input())
# create the dictionary using comprehension
numbers ={n:10*n for n in range(1, n+1) if n >= 3}
print(numbers)


# Example of list comprehension
numbers = [2**i for i in range(1, 6)]
print(numbers)

# Example of lambda function
double = lambda n: n*2
print(double(10))    # 20


# Example of using *args
# *args allows you to pass a variable number of non-keyword arguments to a function
# The function can accept any number of arguments, which are passed as a tuple
def greet(*messages):
    print(messages)
# calling greet() with 1 argument
greet('Hi')
# calling greet() with 2 arguments
greet('Hi', 'Hello')
# calling greet() without any arguments
greet()


# Example of using **kwargs
# **kwargs allows you to pass a variable number of keyword arguments to a function
# The function can accept any number of keyword arguments, which are passed as a dictionary
def print_info(**person):
    print(person)
print_info()
print_info(name = 'Steve')
print_info(name = 'Steve', age = 22)

# Infinite recursion example
def numbers(n):
    print(n)
    numbers(n+1)
numbers(1)
