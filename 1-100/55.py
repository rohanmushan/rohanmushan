# Find the maximum value in a dictionary
# Sample dictionary
my_dict={'a':10,'b':25,'c':15,'d': 40}
# Find the key with the maximum value
max_key = max(my_dict, key=lambda k: my_dict[k])

max_value = my_dict[max_key]

# Print the key and maximum value
print(f"Key with maximum value: {max_key}")
print(f"Maximum value:{max_value}")
