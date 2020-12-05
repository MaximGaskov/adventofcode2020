#!/bin/python3
with open('input', 'r') as input_file:
    codes = input_file.readlines()

seats_ids = []
for code in codes:
    binary_code = code.replace('B', '1').replace('R', '1').replace('F', '0').replace('L', '0')
    row = int(binary_code[:7], 2)
    col = int(binary_code[7:], 2)
    seats_ids.append(row * 8 + col)

print(max(seats_ids))
