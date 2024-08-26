import re

# Function to check if a binary string has more than three consecutive '1's
def has_more_than_three_consecutive_ones(binary_str):
    return bool(re.search(r'1111', binary_str))

# Convert the given binary numbers to integers
binary_numbers = [int("101010", 2), int("011011", 2), int("110100", 2),
                  int("001101", 2), int("100110", 2), int("111111", 2),
                  int("000000", 2)]

# Initialize variables to store the maximum XOR and the corresponding pair
max_xor = 0
max_pair = (None, None)

# Loop through all possible pairs
for i in range(len(binary_numbers)):
    for j in range(i + 1, len(binary_numbers)):
        # Convert the numbers to binary strings
        bin_str_i = format(binary_numbers[i], '06b')
        bin_str_j = format(binary_numbers[j], '06b')
        
        # Check if either of the binary numbers has more than three consecutive '1's
        if (has_more_than_three_consecutive_ones(bin_str_i) or
            has_more_than_three_consecutive_ones(bin_str_j)):
            continue
        
        # Calculate the XOR of the pair
        xor_value = binary_numbers[i] ^ binary_numbers[j]
        
        # Update the maximum XOR and corresponding pair if needed
        if xor_value > max_xor:
            max_xor = xor_value
            max_pair = (bin_str_i, bin_str_j)

# Print the results
if max_pair[0] and max_pair[1]:
    print(f"The pair with the maximum XOR is: {max_pair[0]} and {max_pair[1]}")
    print(f"The maximum XOR value is: {max_xor}")
else:
    print("No valid pair found.")
