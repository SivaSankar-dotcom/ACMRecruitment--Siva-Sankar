def flip_bits(sequence, positions):
    sequence = list(sequence)
    for pos in positions:
        sequence[pos] = '1' if sequence[pos] == '0' else '0'
    return ''.join(sequence)

# Initial sequence
sequence = "10101011010100101110"

# Moves to flip bits
moves = [
    [0, 2, 4],  # Move 1: Flip bits at positions 1, 3, 5
    [7, 9, 11], # Move 2: Flip bits at positions 8, 10, 12
    [13, 16, 18], # Move 3: Flip bits at positions 14, 17, 19
    [9, 11, 13]  # Move 4: Flip bits at positions 10, 12, 14
]

print("Initial sequence:", sequence)
for i, move in enumerate(moves):
    sequence = flip_bits(sequence, move)
    print(f"After move {i+1} (flip positions {move}): {sequence}")
