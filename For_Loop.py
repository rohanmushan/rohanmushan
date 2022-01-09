# Multiplication Table

list = [1,2,3,4,5,6,7,8,9,10]

n = int(input("Enter a number for table: "))

for i in list:
    c = i * n
    print (n,"x",i,"=",c)