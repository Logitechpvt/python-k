
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Number of terms
num_terms = 8
result = fibonacci(num_terms)
print("Fibonacci series:", result)

