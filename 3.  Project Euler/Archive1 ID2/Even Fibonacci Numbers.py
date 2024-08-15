def fibonacci(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total

limit = 4000000
result = fibonacci(limit)
print("Sum of even-valued terms in Fibonacci sequence up to", limit, "is:", result)
