print('Hello from file 2')

def factorial(n):

    return 1 if n == 0 else n * factorial(n - 1)


print(factorial(5))  # Output: 120
