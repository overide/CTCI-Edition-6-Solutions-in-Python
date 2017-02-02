# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

def zero_matrix(matrix):

	# Time Complexity : O(MN)
	# SPace Complexity : O(1)

    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(rows):
        if (matrix[i][0] == 0):
            nullify(matrix, row=i)

    for i in range(cols):
        if (matrix[0][i] == 0):
            nullify(matrix, col=i)


def nullify(matrix, row=None, col=None):
    m = len(matrix)
    n = len(matrix[0])

    if row != None or col != None:
        if(row):
            for i in range(n):
                matrix[row][i] = 0

        if(col):
            for i in range(m):
                matrix[i][col] = 0


def main():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 11, 12], [13, 14, 15, 0]]
    print("Input Matrix\n")
    for row in matrix:
        print(row, "\n")

    zero_matrix(matrix)

    print("Output Matrix\n")
    for row in matrix:
        print(row, "\n")

main()