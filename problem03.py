import string

def count_word_frequency(text):
    # Remove punctuation from the text
    text = text.translate(text.maketrans("", "", string.punctuation))
    # Convert text to lowercase and split it into words
    words = text.lower().split()
    
    # Initialize an empty dictionary to store the word frequencies
    word_frequencies = {}
    
    # Loop through the words
    for word in words:
        # If the word is already a key in the dictionary, increment its count
        if word in word_frequencies:
            word_frequencies[word] += 1
        # Otherwise, add the word to the dictionary with a count of 1
        else:
            word_frequencies[word] = 1
    
    return word_frequencies
