#Check if the two matrices are equal
def identical_matrices(A, B):
    equal = all([a == b for a, b in zip(A, B)])
    if equal:
        print("Matrices are identical")
    else:
        print("Matrices are not identical")
 
A = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
B = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
identical_matrices(A, B)
