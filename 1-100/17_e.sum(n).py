#Calculate the sum of all even numbers between 1 and N.
N=int(input("Enter value of N: "))
sum=0
for i in range(2, N+1,2):
    sum=sum+i
print(f"The sum of even numbers from 1 to {N} is: {sum}")
