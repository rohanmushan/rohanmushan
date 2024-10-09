#Write a program to check if a number is prime.
no=int(input("Enter any number: "))
if(no>1):
    for i in range(2, no):
        if (no%i)==0:
            print(f"{no} is not a prime number")
            break
    else:
        print(f"{no} is a prime number")
else:
    print(f"{no} is not a prime number")
