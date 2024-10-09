# Convert a list of tuples into a dictionary.
# Sample list of tuples
list_of_tuples = [(1, 'one'), (2, 'two'), (3, 'three')]

# Convert the list of tuples into a dictionary
result_dict = {key: value for key, value in list_of_tuples}

# Print the resulting dictionary
print("Resulting Dictionary:", result_dict)
