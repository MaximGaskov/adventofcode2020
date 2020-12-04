def count_trees(right_offset, down_offset, matrix):
    matrix_width = len(matrix[0])
    i, j = (down_offset, right_offset)
    tree_counter = 0

    while i < len(field_matrix):
        if field_matrix[i][j] == '#':
            tree_counter += 1
        i += down_offset
        j = (j + right_offset) % matrix_width
    
    print(i)
    return tree_counter

with open('input') as field_file:
    field_matrix = [[cell for cell in line]  for line in field_file.read().splitlines()]

    result_1_1 = count_trees(1, 1, field_matrix)
    result_3_1 = count_trees(3, 1, field_matrix)
    result_5_1 = count_trees(5, 1, field_matrix)
    result_7_1 = count_trees(7, 1, field_matrix)
    result_1_2 = count_trees(1, 2, field_matrix)

    print(result_1_1 * result_3_1 * result_5_1 * result_7_1 * result_1_2)
