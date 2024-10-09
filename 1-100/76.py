# Remove a key-value pair from a dictionary.
#using del fun:
# Sample dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Key to remove
key_to_remove = 'age'

# Remove the key-value pair from the dictionary using the del statement
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"'{key_to_remove}' key-value pair removed from the dictionary.")
else:
    print(f"'{key_to_remove}' key not found in the dictionary.")
#OR

#using pop()

# Sample dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Key to remove
key_to_remove = 'age'

# Remove the key-value pair from the dictionary using the pop() method
if key_to_remove in my_dict:
    removed_value = my_dict.pop(key_to_remove)
    print(f"'{key_to_remove}' key-value pair with value '{removed_value}' removed from the dictionary.")
else:
    print(f"'{key_to_remove}' key not found in the dictionary.")
