
total = 0

for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
        total += n

print("The sum of all multiples of 3 or 5 below 1000 is:", total)
