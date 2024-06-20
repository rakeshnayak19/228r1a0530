# Function to read a matrix from user input
def read_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(int(input(f"Enter element at position ({i+1},{j+1}): ")))
        matrix.append(row)
    return matrix

# Function to add two matrices
def add_matrices(matrix1, matrix2, rows, columns):
    result = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Read dimensions for the matrices (both matrices must have the same dimensions)
r = int(input("Enter the number of rows for the matrices: "))
c = int(input("Enter the number of columns for the matrices: "))

print("Enter the elements for the first matrix:")
A = read_matrix(r, c)

print("\nEnter the elements for the second matrix:")
B = read_matrix(r, c)

# Add the two matrices
C = add_matrices(A, B, r, c)

# Print the matrices
print("\nThe first matrix is:")
for row in A:
    print(row)

print("\nThe second matrix is:")
for row in B:
    print(row)

print("\nThe resulting matrix after addition is:")
for row in C:
    print(row)
