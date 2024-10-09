# Merge two dictionaries while summing values for common keys.
# Function to merge two dictionaries while summing values for common keys
def merge_and_sum_dicts(dict1, dict2):
    result_dict = dict1.copy()  # Create a copy of the first dictionary

    for key, value in dict2.items():
        if key in result_dict:
            result_dict[key] += value
        else:
            result_dict[key] = value

    return result_dict

# Sample dictionaries
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

# Merge and sum the dictionaries
merged_dict = merge_and_sum_dicts(dict1, dict2)

# Print the merged dictionary
print("Merged Dictionary with Summed Values:")
print(merged_dict)
