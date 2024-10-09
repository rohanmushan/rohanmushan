# Merge two dictionaries and handle duplicate keys by concatenating values into lists.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

# Merge the dictionaries while handling duplicate keys
merged_dict = {}
for key, value in dict1.items():
    if key in dict2:
        # If the key exists in both dictionaries, concatenate values into a list
        merged_dict[key] = [value, dict2[key]]
    else:
        merged_dict[key] = value

for key, value in dict2.items():
    if key not in dict1:
        # Add keys from the second dictionary that are not in the first dictionary
        merged_dict[key] = value

# Print the merged dictionary
print("Merged Dictionary with Concatenated Values:")
print(merged_dict)
