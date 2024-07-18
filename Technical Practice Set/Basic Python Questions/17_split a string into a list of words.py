# Using the split() Method


def split_string_into_words(input_string):
    # Use split() method to split the string into a list of words
    words_list = input_string.split()
    return words_list

# Example usage
sentence = "Hello world this is a test"
words = split_string_into_words(sentence)
print(words)  # Output: ['Hello', 'world', 'this', 'is', 'a', 'test']
