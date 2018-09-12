def incrementing_matrix(rows):
    # matrix = list(range(0,6))
    matrix = []
    i = 0
    while i < rows:
        row = list(range(i,i+rows))
        matrix.append(row)
        i += 1
    return(matrix)


matrix = incrementing_matrix(10)
for element in matrix:
    print(element)
