
# Function to find the largest word in a sentence
def find_largest_word(sentence):
    # Split the sentence into words
    words=sentence.split()
    if not words:
        return None  # Return None if the sentence is empty

    # Initialize variables to track the largest word and its length
    largest_word=words[0]
    largest_length=len(largest_word)

    # Iterate through the words in the sentence
    for word in words:
        # Remove punctuation from the word (optional)
        word=word.strip(".,!?;")

        # Compare the length of the current word with the largest word
        if len(word)>largest_length:
            largest_word=word
            largest_length=len(word)

    return largest_word

# Input sentence
my_sentence="The quick brown fox jumped over the lazy dog."

# Find the largest word in the sentence
largest_word=find_largest_word(my_sentence)

if largest_word:
    print(f"The largest word in the sentence is: '{largest_word}'")
else:
    print("The sentence is empty.")
