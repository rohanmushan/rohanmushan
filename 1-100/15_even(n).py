#Print even numbers from 1 to N using a for loop.

N=int(input("Enter value of N: "))
print(f"The even numbers from 1 to {N} are:")
for i in range(2, N+1,2):
    print(i)
