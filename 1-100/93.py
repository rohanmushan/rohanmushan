# Create a list of unique elements from a list of lists.
from itertools import chain

# Sample list of lists
list_of_lists = [[1, 2, 3], [3, 4, 5], [5, 6, 7, 8]]

# Create a list of unique elements using itertools.chain and set
unique_elements = list(set(chain(*list_of_lists)))

# Print the list of unique elements
print("List of Unique Elements:", unique_elements)
