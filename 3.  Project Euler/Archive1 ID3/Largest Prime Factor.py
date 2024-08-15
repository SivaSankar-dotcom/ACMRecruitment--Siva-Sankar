n = 600851475143
i = 2
while i * i <= n:
    if n % i:
        i += 1
    else:
        n //= i

print("The largest prime factor of 600851475143 is",n)
