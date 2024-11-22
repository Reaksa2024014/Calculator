# Create a 2D list representing a 3x3 grid
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)


# Access the element in the second row, third column
print(matrix[1][2])

# Modifying Elements in a 2D List
# Change the element at the third row, second column to 10
matrix[2][1] = 10


# Using Loops to Traverse a 2D List
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()


# Read Index of elements
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(f"Element at position ({row}, {col}) is {matrix[row][col]}")


#  Calculate the sum of each row in a 2D list.
row_sums = [sum(col) for col in matrix]
print(row_sums)


# sums of each column
column_sums = [0, 0, 0]

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        column_sums[col] += matrix[row][col]

print(column_sums)
