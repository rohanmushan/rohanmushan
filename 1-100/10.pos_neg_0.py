#Write a program to check if a number is positive, negative, or zero.
no=int(input("Enter a Number: "))
if(no>0):
    print(f"{no} is Positive")
elif(no<0):
    print(f"{no} is negative")
else:
    print(f"{no} is Zero")
