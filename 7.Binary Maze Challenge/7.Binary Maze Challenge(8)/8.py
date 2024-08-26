def has_four_ones(binary_str):
    return binary_str.count('1') == 4
results = []
for i in range(1024):
    binary_str = format(i, '010b')
    if has_four_ones(binary_str):
        results.append((binary_str, i))
for binary_str, decimal in results:
    print(f"Binary: {binary_str}, Decimal: {decimal}")
