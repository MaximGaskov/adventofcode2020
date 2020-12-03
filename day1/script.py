with open('input', 'r') as report_file:
    report_lines = report_file.readlines()

report_numbers = list(map(int, report_lines))
for index1, el1 in enumerate(report_numbers):
     for index2 in range(index1, len(report_numbers)):
             el2 = report_numbers[index2]
             if el1 + el2 == 2020:
                     print(el1 * el2)
                     exit()
