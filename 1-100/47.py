#Extract a submatrix from a larger matrix
import numpy as np
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]])

print(arr)
print('-' * 50)
submatrix = arr[np.ix_([0, 3], [1, 3])]
print(submatrix)
