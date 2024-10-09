#Check if an element exists in a list
numbers=[5, 10, 15, 20, 25]
check=int(input("Enter num to check: "))
if(check in numbers):
    print(f"{check} exists in the list.")
else:
    print(f"{check} does not exist in the list.")
