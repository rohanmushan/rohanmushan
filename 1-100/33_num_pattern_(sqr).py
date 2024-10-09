#Print a pattern of numbers in a square.

size=int(input("Enter the size of the square: "))
for i in range(1, size+1):
    for j in range(1, size+1):
        print((i+j-1) % size+1, end=" ")
    print()
