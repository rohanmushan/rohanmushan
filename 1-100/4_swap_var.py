#Write a program to swap two variables.

var1 = input("Enter the value for the first variable: ")
var2 = input("Enter the value for the second variable: ")
print(f"Before swapping: var1 = {var1}, var2 = {var2}")
var1, var2= var2, var1
print(f"After swapping: var1 = {var1}, var2 = {var2}")
