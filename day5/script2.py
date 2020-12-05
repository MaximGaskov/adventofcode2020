#!/bin/python3
with open('input', 'r') as input_file:
    codes = input_file.readlines()

seats_ids = []
for code in codes:
    binary_code = code.replace('B', '1').replace('R', '1').replace('F', '0').replace('L', '0')
    row = int(binary_code[:7], 2)
    col = int(binary_code[7:], 2)
    seats_ids.append(row * 8 + col)

seats_ids.sort()
for i in range(len(seats_ids) - 1):
    if seats_ids[i + 1] - seats_ids[i] == 2:
        print(seats_ids[i] + 1)
