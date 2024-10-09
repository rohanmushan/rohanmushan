#Check if a number is a perfect number
num=int(input("Enter number: "))
sum1=0
for i in range(1, n):
    if(num%i==0):
        sum1=sum1+i
if(sum1==n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")
