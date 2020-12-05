#!/usr/bin/python3
import re
import sys

def params_are_valid(entity):
    if len(re.findall('(byr|iyr|eyr|hgt|hcl|ecl|pid):', entity)) != 7:
        return False

    params = dict([ (e.split(':')) for e in entity.split(' ') ])

    if ((1920 <= int(params['byr']) <= 2002) and
            (2010 <= int(params['iyr']) <= 2020) and
            (2020 <= int(params['eyr']) <= 2030) and
            (('cm' in params['hgt'] and 150 <= int(params['hgt'][:-2]) <= 193) or
                ('in' in params['hgt'] and 59 <= int(params['hgt'][:-2]) <= 76)) and
            (re.match('#(\d|[a-f]){6}$', params['hcl'])) and
            (params['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and
            (re.match('[0-9]{9}$', params['pid']))):
        return True
    return False

with open('input') as input_file:
    entities = input_file.read()[:-1].split('\n\n')

valid_passport_counter = 0
for entity in [e.replace('\n', ' ') for e in entities]:
    if params_are_valid(entity):
        valid_passport_counter += 1

print(valid_passport_counter)

    

