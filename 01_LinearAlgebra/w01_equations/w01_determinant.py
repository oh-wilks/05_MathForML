def calculate_determinant(matrix):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError("The matrix must be square")

    # Base case: for a 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    sign = 1

    # Iterate over the first row of the matrix
    for col in range(len(matrix[0])):
        # Exclude the current column from the submatrix
        submatrix = [row[:col] + row[col + 1:] for row in matrix[1:]]

        # Recursive call to calculate the determinant of the submatrix
        sub_determinant = calculate_determinant(submatrix)

        # Add or subtract the product of the element and its sub_determinant
        determinant += sign * matrix[0][col] * sub_determinant
        sign = -sign

    return determinant

'''
example
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
'''
matrix = [[2, 3],
          [2, 4],]

det = calculate_determinant(matrix)
print("Determinant:", det)
