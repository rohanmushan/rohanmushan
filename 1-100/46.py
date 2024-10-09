#Implement matrix addition and subtraction.
import numpy as np
m1 = np.array([[1, 3, 4], [8, 5, 6]])
m2 = np.array([[8, 6, 9], [9, 0, 6]])

print("Add Matrix:")
a = np.add(m1, m2)
print(a)

print("Subtract Matrix:")
b = np.subtract(m2, m1)
print(b)
