import fibonacci_module

n = int(input("Enter how many Fibonacci numbers to generate: "))
fib_numbers = fibonacci_module.fibonacci(n)

print("Fibonacci sequence:")
for num in fib_numbers:
    print(num, end=" ")