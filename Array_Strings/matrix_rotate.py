# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this
# in place?


def inplace_rotate(matrix):
    '''
    time complexity = O(N^2)
    space complexity = O(1)
    '''
    if matrix == None or len(matrix) != len(matrix[0]):
        return False
    else:
        for layer in range(len(matrix) // 2):
            first = layer
            last = len(matrix) - 1 - layer
            for i in range(first, last):
                offset = i - first
                top = matrix[first][i]
                matrix[first][i] = matrix[last - offset][first]
                matrix[last - offset][first] = matrix[last][last - offset]
                matrix[last][last - offset] = matrix[i][last]
                matrix[i][last] = top

    return matrix


def main():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("Input Matrix\n")
    for row in matrix:
        print(row, "\n")
    matrix = inplace_rotate(matrix)
    print("\nRotated Matrix\n")
    for row in matrix:
        print(row, "\n")

main()
