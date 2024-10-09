# Find the common elements between the two dictionaries.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}

# Find the common elements between the two dictionaries
common_elements = {key: dict1[key] for key in dict1 if key in dict2 and dict1[key] == dict2[key]}

# Print the common elements
print("Common Elements Between the Dictionaries:", common_elements)
