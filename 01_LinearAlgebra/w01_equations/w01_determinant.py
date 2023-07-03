def calculate_determinant(matrix, indent=""):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError("The matrix must be square")

    # Base case: for a 2x2 matrix
    if len(matrix) == 2:
        print(f"{indent}Calculating determinant of 2x2 matrix:")
        print(f"{indent}{matrix[0][0]} * {matrix[1][1]} - {matrix[0][1]} * {matrix[1][0]}")
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        print(f"{indent}Determinant: {determinant}")
        return determinant

    determinant = 0
    sign = 1

    # Iterate over the first row of the matrix
    for col in range(len(matrix[0])):
        print(f"{indent}Calculating determinant of {len(matrix)}x{len(matrix)} matrix:")
        print(f"{indent}Current column: {col}")
        
        # Exclude the current column from the submatrix
        submatrix = [row[:col] + row[col + 1:] for row in matrix[1:]]

        print(f"{indent}Submatrix:")
        for row in submatrix:
            print(f"{indent}{row}")
        
        # Recursive call to calculate the determinant of the submatrix
        print(f"{indent}Recursive call to calculate determinant of submatrix:")
        sub_determinant = calculate_determinant(submatrix, indent + "  ")
        print(f"{indent}Sub-determinant: {sub_determinant}")

        # Add or subtract the product of the element and its sub_determinant
        print(f"{indent}Adding or subtracting: {sign} * {matrix[0][col]} * {sub_determinant}")
        determinant += sign * matrix[0][col] * sub_determinant
        sign = -sign

    print(f"{indent}Determinant: {determinant}")
    return determinant


matrix = [[1, 2, 3],
          [0, 2, 2],
          [1, 4, 5]]

det = calculate_determinant(matrix)
print("Determinant:", det)
