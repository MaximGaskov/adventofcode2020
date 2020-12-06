#!/bin/python3
with open('input', 'r') as input_file:
    answer_groups = input_file.read().split('\n\n')

sum_of_unique_answers = 0
for answer_group in answer_groups:
    sum_of_unique_answers += len(set(answer_group.replace('\n', '')))
print(sum_of_unique_answers)
