#!/bin/python3
with open('input', 'r') as input_file:
    answer_groups = input_file.read()[:-1].split('\n\n')

sum_of_unique_answers = 0
for answer_group in answer_groups:
    answer_group_sets = [set(s) for s in answer_group.split('\n')]
    sum_of_unique_answers += len(set.intersection(*answer_group_sets))
print(sum_of_unique_answers)
