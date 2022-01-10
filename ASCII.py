# Program to find the ASCII value of the character 'X' and 'x'

c="X"
b="x"
print("The ASCII value of "+ c + "is:", ord(c))
print("The ASCII value of "+ b + "is:", ord(b))

# Write a program to compute Quotient and Remainder

a=5
b=6

q = a// b
print("Quotient:",q)

r = a % b
print("Remainder:",r)

# Swap two numbers using temporary variable

x=6
y=7

temp=x
x = y 
y = temp

print("x value after swapping is",x)
print("y value after swapping is",y)

# Write program to check whether a number is even or odd  88,37,1658

x=88371658

if ( x % 2 ) == 0 :
    print("Number is even",x)
else:
    print("Number is odd",x)

# Check whether an alphabet is vowel or consonant if..else statement -a,b,e,o

x="a"

if x in ('a','e','i','o','u'):
    print("The given alphabet is vowel",x)
else:
    print("The given alphabet is consonant",x)

 # Write program to calculate GST i.e 18% on base price 34900/-

gst = ((18/100) * 34900)
print("gst is",gst)

# write program to calculate montly simple interest and compund interest (5%Month) on amount - 161258/-

p=161258
r=6
t=1

si=p*r*t*0.01

print("si:",si)

Amount = p * (pow((1 + r / 100),t))
ci = Amount - p
print("Compound interest is",ci)

# Write program to calculate montly simple interest and compound interest (5%Month) on amount - 161258/-

a = 161258

e3 = a/36

e5 = a/60

emi3=e3+(0.05*e3)
 
emi5=e5+(0.05*e5)

print("EMI for 3 years with interest 5% ",emi3)
 
print("EMI for 5 years with interest 5% ",emi5)