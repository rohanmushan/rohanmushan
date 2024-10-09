# Remove all occurrences of a specific element from a list
my_list = [1, 2, 3, 2, 4, 5, 2]

# Element to remove
element_to_remove = 2

# Remove all occurrences of the element from the list
new_list = [x for x in my_list if x != element_to_remove]

# Print the new list
print("Original List:", my_list)
print("List with Element Removed:", new_list)
