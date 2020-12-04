with open('input') as field_file:
    field_matrix = [[cell for cell in line]  for line in field_file.read().splitlines()]
    matrix_width = len(field_matrix[0])

    i, j = (1,3)
    tree_counter = 0
    
    while i < len(field_matrix):
        if field_matrix[i][j] == '#':
            tree_counter += 1 
        i += 1
        j = (j + 3) % matrix_width


print(tree_counter)
