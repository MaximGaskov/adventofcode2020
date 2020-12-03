with open('input', 'r') as report_file:
    report_lines = report_file.readlines()

report_numbers = list(map(int, report_lines))


def two_numbers(values, desired_sum):
    if len(values) < 2:
        exit()
    for index1, el1 in enumerate(values):
         for index2 in range(index1 + 1, len(values)):
                 el2 = values[index2]
                 if el1 + el2 == desired_sum:
                     return (el1, el2)

for index0, el0 in enumerate(report_numbers):
    two_num_res = two_numbers(report_numbers[index0 + 1:], 2020 - el0)
    if not two_num_res:
        continue
    el1, el2 = two_num_res
    if el0 + el1 + el2 == 2020:
        print(el0 * el1 * el2)
        exit()
        

