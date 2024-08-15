def sample(n):
    for a in range(1, n // 3):
        for b in range(a + 1, n// 2):
            c = n- a - b
            if a * a + b * b == c * c:
                return a, b, c


n = 1000


triplet = sample(n)

if triplet:
    a, b, c = triplet
    product = a * b * c
    print(f"The Pythagorean triplet is: a = {a}, b = {b}, c = {c}")
    print(f"The product abc is: {product}")
else:
    print("No Pythagorean triplet found.")
