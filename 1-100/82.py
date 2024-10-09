# Find the second largest element in a list.

my_list = [10, 20, 5, 30, 15]

# Sort the list in ascending order
sorted_list = sorted(my_list)

# Find the second largest element
if len(sorted_list) >= 2:
    second_largest = sorted_list[-2]
    print("Second Largest Element:", second_largest)
else:
    print("The list does not have a second largest element.")
