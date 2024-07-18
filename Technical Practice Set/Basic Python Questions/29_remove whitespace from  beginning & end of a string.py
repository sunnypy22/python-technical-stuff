# Using strip()


def remove_whitespace(input_string):
    return input_string.strip()

# Example usage
input_string = "   Hello, world!   "
result = remove_whitespace(input_string)
print("Original string:", repr(input_string))  # Output: Original string: '   Hello, world!   '
print("String with whitespace removed:", repr(result))  # Output: String with whitespace removed: 'Hello, world!'
