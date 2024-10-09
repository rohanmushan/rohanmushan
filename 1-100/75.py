# Check if a given key exists in a dictionary.

#Using the in operator:
# Sample dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Key to check
key_to_check = 'age'

# Check if the key exists in the dictionary
if key_to_check in my_dict:
    print(f"'{key_to_check}' exists in the dictionary.")
else:
    print(f"'{key_to_check}' does not exist in the dictionary.")
Using the get() method:

#OR
#Using the get operator:
# Sample dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Key to check
key_to_check = 'age'

# Check if the key exists in the dictionary using the get() method
if my_dict.get(key_to_check) is not None:
    print(f"'{key_to_check}' exists in the dictionary.")
else:
    print(f"'{key_to_check}' does not exist in the dictionary.")
