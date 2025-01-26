# Initial values
number1 = 10  # In binary: 1010
number2 = 4   # In binary: 0100
# Bitwise AND
result = number1 & number2
print(f"Bitwise AND of {number1} & {number2} = {result}")  # 1010 & 0100 = 0000 (result = 0)
# Bitwise OR
result = number1 | number2
print(f"Bitwise OR of {number1} | {number2} = {result}")   # 1010 | 0100 = 1110 (result = 14)
# Bitwise XOR
result = number1 ^ number2
print(f"Bitwise XOR of {number1} ^ {number2} = {result}")  # 1010 ^ 0100 = 1110 (result = 14)
# Bitwise NOT
result = ~number1
print(f"Bitwise NOT of ~{number1} = {result}")             # ~1010 = -1011 (result = -11)
# Bitwise Left Shift
result = number1 << 2
print(f"Left Shift of {number1} << 2 = {result}")          # 1010 << 2 = 101000 (result = 40)
# Bitwise Right Shift
result = number1 >> 2
print(f"Right Shift of {number1} >> 2 = {result}")
