#Find the determinant of a square matrix
import numpy as np

n_array = np.array([[50, 29], [30, 44]]) 
print("Numpy Matrix is:") 
print(n_array) 
   
det = np.linalg.det(n_array) 
print("\nDeterminant of given 2X2 matrix:") 
print(int(det))
