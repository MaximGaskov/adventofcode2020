import re

with open('input', 'r') as input_file:
    passwd_lines = input_file.readlines()

valid_passwd_counter = 0
for passwd_line in passwd_lines:
    line_regex = re.search("(\d+)-(\d+)\s([a-zA-Z]):\s(.*)", passwd_line)

    lower_index = int(line_regex.group(1))
    higher_index = int(line_regex.group(2))
    required_letter = line_regex.group(3)
    passwd = line_regex.group(4)
    
    if (passwd[lower_index - 1] == required_letter) ^ (passwd[higher_index - 1] == required_letter):
        valid_passwd_counter += 1

print(valid_passwd_counter)
