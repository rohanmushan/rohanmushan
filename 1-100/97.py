# .Remove all punctuation from a string.
import string

# Sample string with punctuation
my_string = "This is a sample string with punctuation! Do you see? No punctuation."

# Create a translation table to remove punctuation
translator = str.maketrans('', '', string.punctuation)

# Remove all punctuation from the string using translate()
my_string = my_string.translate(translator)

# Print the string with punctuation removed
print("String with Punctuation Removed:", my_string)
