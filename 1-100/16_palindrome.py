#Write a program to check if a number is a palindrome.
num=int(input("Enter a number: "))
num=str(num)
reversed_str=num[::-1]
if (num==reversed_str):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
