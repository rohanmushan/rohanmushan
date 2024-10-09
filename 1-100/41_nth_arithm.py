#Calculate the nth term of an arithmetic progression

a=int(input("Enter First Number of an A.P Series: : "))
n=int(input("Please Enter the Total Numbers in this A.P Series: : "))
d=int(input("Please Enter the Common Difference : "))
total=(n*(2*a+(n-1)*d)) / 2
tn=a+(n-1)*d
print("\nSum of Arithmetic Progression Series = " , total)
print("tn Term of Arithmetic Progression Series = " , tn)
