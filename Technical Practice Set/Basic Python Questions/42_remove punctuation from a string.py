# 1. Using string.punctuation and str.translate()

'''You can utilize the string.punctuation constant from the string module along with
 str.translate() method to remove punctuation characters.'''


import string

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

# Example usage
input_string = "Hello, world! This is a test string."
cleaned_string = remove_punctuation(input_string)
print(f"Original string: {input_string}")
print(f"String without punctuation: {cleaned_string}")

# 2. Using Regular Expressions (re module)

'''Regular expressions provide a flexible way to remove
 specific patterns from strings, including punctuation.'''

import re

def remove_punctuation_regex(input_string):
    return re.sub(r'[^\w\s]', '', input_string)

# Example usage
input_string = "Hello, world! This is a test string."
cleaned_string = remove_punctuation_regex(input_string)
print(f"Original string: {input_string}")
print(f"String without punctuation: {cleaned_string}")

# 3. Iterating Through Characters

'''You can iterate through each character in the string and build a
 new string excluding punctuation characters.'''

def remove_punctuation_iterative(input_string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    cleaned_string = ""
    for char in input_string:
        if char not in punctuations:
            cleaned_string += char
    return cleaned_string

# Example usage
input_string = "Hello, world! This is a test string."
cleaned_string = remove_punctuation_iterative(input_string)
print(f"Original string: {input_string}")
print(f"String without punctuation: {cleaned_string}")
