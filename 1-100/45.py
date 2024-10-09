#Find the sum of the main diagonal elements of a matrix.
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[1,2,3,4],
     [5,6,7,8],
     [2,4,6,8]]

result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
       for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print('Multiplied Matrix:')
for r in result:
    print(r)
