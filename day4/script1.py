import re

with open('input') as input_file:
    entities = input_file.read().split('\n\n')

valid_passport_counter = 0
for entity in [e.replace('\n', ' ') for e in entities]:
    if len(re.findall('(byr|iyr|eyr|hgt|hcl|ecl|pid):', entity)) == 7:
        valid_passport_counter += 1

print(valid_passport_counter)
