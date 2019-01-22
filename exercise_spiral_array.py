def calc_matrix(square_size):
    matrix = [[""] * square_size for i in range(square_size)]
    remaining_ints = [(n) for n in range(square_size**2, 0, -1)]
    tier = 0
    cursor = [0,0]
    while remaining_ints:
        for top_idx in range(tier, square_size - tier):
            if remaining_ints:
                matrix[tier][top_idx] = remaining_ints.pop()
                cursor = [tier, top_idx]
        for right_idx in range(tier + 1, square_size - tier):
            if remaining_ints:
                matrix[right_idx][cursor[1]] = remaining_ints.pop()
                cursor = [right_idx, cursor[1]]
        for bottom_idx in range(square_size - tier - 2 , tier-1, -1):
            if remaining_ints:
                matrix[cursor[0]][bottom_idx] = remaining_ints.pop()
                cursor = [cursor[0], bottom_idx]
        for left_idx in range(square_size - tier - 2 , tier, -1):
            if remaining_ints:
                matrix[left_idx][cursor[1]] = remaining_ints.pop()
                cursor = [[left_idx], cursor[1]]
        tier += 1

    return(matrix)

print(calc_matrix(6))



