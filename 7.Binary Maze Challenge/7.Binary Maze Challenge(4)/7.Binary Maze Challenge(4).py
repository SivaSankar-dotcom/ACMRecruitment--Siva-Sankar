# Define the binary weights
weights = [
    '1001', '1100', '1110', '1010', '0111',
    '0101', '0011', '1111', '1101', '1011',
    '0110', '0100', '0010', '0001', 'unknown_heavier'
]

# Convert binary weights to integers, except the unknown heavier one
weights_int = [int(w, 2) if w != 'unknown_heavier' else None for w in weights]

# Function to simulate weighing groups
def weigh_groups(group1, group2):
    weight1 = sum(w for w in group1 if w is not None)
    weight2 = sum(w for w in group2 if w is not None)
    if weight1 > weight2:
        return 1
    elif weight1 < weight2:
        return -1
    else:
        return 0

# Divide weights into three groups
group1 = weights_int[:5]
group2 = weights_int[5:10]
group3 = weights_int[10:]

# Weigh the groups
result = weigh_groups(group1, group2)
if result == 0:
    heavier_group = group3
elif result == 1:
    heavier_group = group1
else:
    heavier_group = group2

# Further divide the heavier group
group1 = heavier_group[:2]
group2 = heavier_group[2:]

# Weigh the smaller groups
result = weigh_groups(group1, group2)
if result == 0:
    heavier_item = heavier_group[-1]
elif result == 1:
    heavier_item = group1[0] if group1[0] is not None else group1[1]
else:
    heavier_item = group2[0] if group2[0] is not None else group2[1]

# Output the heaviest item
print(f"The heaviest binary number is: {bin(heavier_item)[2:]}")
