# Find the length of the longest word in a list of words
# Sample list of words
word_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Initialize a variable to store the length of the longest word
longest_word_length = 0

# Iterate through the list of words
for word in word_list:
    word_length = len(word)
    if word_length > longest_word_length:
        longest_word_length = word_length

# Print the length of the longest word
print("Length of the Longest Word:", longest_word_length)
