# Using title() Method

def capitalize_first_letter_title(input_string):
    return input_string.title()

# Example usage
input_string = "hello world! this is a test string."
capitalized_string = capitalize_first_letter_title(input_string)
print("Original string:", input_string)
print("Capitalized string:", capitalized_string)

# Using Splitting and Joining

def capitalize_first_letter_split_join(input_string):
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

# Example usage
input_string = "hello world! this is a test string."
capitalized_string = capitalize_first_letter_split_join(input_string)
print("Original string:", input_string)
print("Capitalized string:", capitalized_string)
