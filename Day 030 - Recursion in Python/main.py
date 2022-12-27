# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1


# factorial(n) = n * factorial(n-1)
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....

# Python program to generate Fibonacci series Program using Recursion


def fibonacci(num):
    if num < 0:
        print("Invalid Syntax")
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return (fibonacci(num - 1) + fibonacci(num - 2))


number = int(input("Enter the terms: "))
print("Fibonacci Series: ", end=' ')
for n in range(number):
    print(fibonacci(n), end=' ')
