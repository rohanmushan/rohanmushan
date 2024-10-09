# Find the keys with the highest values in a dictionary.
# Function to find keys with the highest values in a dictionary
def keys_with_highest_values(input_dict):
    max_value = max(input_dict.values())
    highest_value_keys = [key for key, value in input_dict.items() if value == max_value]
    return highest_value_keys

# Sample dictionary
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 20}

# Find the keys with the highest values
highest_value_keys = keys_with_highest_values(my_dict)

# Print the keys with the highest values
print("Keys with the Highest Values:", highest_value_keys)
