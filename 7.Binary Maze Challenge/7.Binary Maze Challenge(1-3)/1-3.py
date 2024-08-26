
binary1 = '1100101011110010'
binary2 = '1010110010101101'
binary3 = '0111001100110011'
binary4 = '1101110111001110'

num1 = int(binary1, 2)
num2 = int(binary2, 2)
num3 = int(binary3, 2)
num4 = int(binary4, 2)

result = num1 & num2
result_binary = bin(result)[2:]  
print("The result of the AND operation is:", result_binary)

or_result = result | num3
or_result_binary = bin(or_result)[2:]
print("The result of the OR operation is:", or_result_binary)

xor_result = or_result ^ num4
xor_result_binary = bin(xor_result)[2:]
print(f"The result of the XOR operation is: {xor_result_binary}")

not_result = ~xor_result
not_result_binary = bin(not_result & 0xFFFF)[2:]
print(f"The result of the NOT operation is: {not_result_binary}")

      
final_result_binary = '1101100110000010'
final_result_decimal = int(final_result_binary, 2)
print(f"The decimal form of the final result is: {final_result_decimal}")

added_result = final_result_decimal + 123
print(f"The result after adding 123 is: {added_result}")

multiplied_result = added_result * 7
print(f"The result after multiplying by 7 is: {multiplied_result}")


final_result_binary = bin(multiplied_result)[2:]
print(f"The final result in binary is: {final_result_binary}")
