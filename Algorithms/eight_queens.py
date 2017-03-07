# Eight non-conflicting Queen problem
# Algorithm involves adding a Queen in each row
# Insuring no conflicts with queens in columns or diagonals
def queensproblem(rows, columns):
    
    solutions = [[]]

    # Adding queens to every row
    for row in range(rows):
        solutions = add_one_queen(row, columns, solutions)
    return solutions 

# Adding a single queen to a specefied row
def add_one_queen(new_row, columns, prev_solutions):
    return [solution + [new_column]
            for solution in prev_solutions
            for new_column in range(columns)
            if no_conflict(new_row, new_column, solution)]

# Looking for conflicts
def no_conflict(new_row, new_column, solution):
    return all(solution[row]       != new_column           and
               solution[row] + row != new_column + new_row and
               solution[row] - row != new_column - new_row
               for row in range(new_row))

for solution in queensproblem(8, 8):
    print(solution)

