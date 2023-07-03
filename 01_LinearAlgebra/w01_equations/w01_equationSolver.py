
# linear equation solver
def solve_linear_system(A, b):
    n = len(A)
    
    # Perform Gaussian elimination
    for i in range(n):
        pivot = A[i][i]
        
        # Divide the current row by the pivot
        for j in range(n):
            A[i][j] /= pivot
        b[i] /= pivot
        
        # Eliminate the values below the pivot
        for k in range(i + 1, n):
            factor = A[k][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            b[k] -= factor * b[i]
    
    # Back substitution to find the solution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
    
    return x


# Define the coefficients of the linear system
'''
A = [[a11x1 + a12x2 + ... + a1n*xn ], [a21x1 + a22x2 + ... + a2n*xn ]]
b = [b1, b2.. bm]

example
3x - 2y = 8
2x -  y = 3

A = [[3, 2], [2, -1]]
b = [8, 3]

'''

A = [[2, 5], [8, 1]]
b = [46, 32]

# Solve the linear system
x = solve_linear_system(A, b)

# Print the solution
print("Solution: x =", x)
