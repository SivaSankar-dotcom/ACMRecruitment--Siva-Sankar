def sample(n):
    x = 0
    for i in range(1, n + 1):
        x += i
        
    a = x ** 2
    b = 0  
    for i in range(1, n + 1):
        b += i ** 2

    difference = a - b
    return difference

print("The difference is:", sample(100))
