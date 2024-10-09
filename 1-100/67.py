# Create a dictionary of words and their frequencies in a text
# Function to create a dictionary of word frequencies in a text
def word_frequency(text):
    word_dict = {}
    words = text.split()

    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitive counting
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict

# Sample text
my_text = "This is a sample text. This text contains sample words."

# Create a dictionary of word frequencies
word_frequencies = word_frequency(my_text)

# Print the word frequencies
for word, frequency in word_frequencies.items():
    print(f"{word}: {frequency}")
