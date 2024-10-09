# Combine two dictionaries, preserving the original keys
# Using dictionary unpacking (**):
# Sample dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Combine the dictionaries using dictionary unpacking
combined_dict = {**dict1, **dict2}

# Print the combined dictionary
print("Combined Dictionary:", combined_dict)
#OR
#Using a loop to merge dictionaries:
# Sample dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Combine the dictionaries while preserving original keys
combined_dict = dict1.copy()  # Start with a copy of dict1

for key, value in dict2.items():
    if key not in combined_dict:
        combined_dict[key] = value

# Print the combined dictionary
print("Combined Dictionary:", combined_dict)
