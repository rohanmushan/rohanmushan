#Print a pattern of numbers in an equilateral triangle.

rows=int(input("Enter rows for the triangle: "))
for i in range(1, rows+1):
    print(" " * (rows - i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()
