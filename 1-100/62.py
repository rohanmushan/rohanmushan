# Reverse the order of words in a sentence
# Function to reverse the order of words in a sentence
def reverse_words(sentence):
    # Split the sentence into words
    words=sentence.split()

    # Reverse the order of words
    reversed_words=words[::-1]

    # Join the reversed words to form the new sentence
    reversed_sentence=' '.join(reversed_words)

    return reversed_sentence

# Input sentence
my_sentence="The quick brown fox"

# Reverse the order of words in the sentence
reversed_sentence=reverse_words(my_sentence)

print("Original Sentence:", my_sentence)
print("Reversed Sentence:", reversed_sentence)
