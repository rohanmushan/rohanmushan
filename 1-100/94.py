# Find the first non-repeated character in a string.
# Function to find the first non-repeated character in a string
def find_first_non_repeated_char(input_string):
    char_count = {}
    
    # Count occurrences of each character in the string
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first non-repeated character
    for char in input_string:
        if char_count[char] == 1:
            return char
    
    return None  # Return None if there are no non-repeated characters

# Sample string
my_string = "programming"

# Find the first non-repeated character in the string
first_non_repeated_char = find_first_non_repeated_char(my_string)

if first_non_repeated_char is not None:
    print(f"The first non-repeated character is: {first_non_repeated_char}")
else:
    print("There are no non-repeated characters in the string.")
