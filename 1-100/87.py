# Find the index of the first occurrence of a specific element in a list.
my_list = [10, 20, 30, 40, 50, 20, 60]

# Element to find
element_to_find = 20

# Find the index of the first occurrence of the element
try:
    index = my_list.index(element_to_find)
    print(f"Index of the first occurrence of {element_to_find}: {index}")
except ValueError:
    print(f"{element_to_find} not found in the list.")
