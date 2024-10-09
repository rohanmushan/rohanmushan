# Check if a string is a palindrome.
def is_palindrome(input_string):
    clean_string=input_string.replace(" ", "").lower()
    
    # Check if the cleaned string is equal to its reverse
    return clean_string==clean_string[::-1]


my_string="racecar"
if is_palindrome(my_string):
    print(f"'{my_string}' is a palindrome.")
else:
    print(f"'{my_string}' is not a palindrome.")
