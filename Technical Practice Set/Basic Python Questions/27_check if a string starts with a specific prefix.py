# 1. Using str.startswith()

def starts_with_using_startswith(string, prefix):
    return string.startswith(prefix)

# Example usage
string = "Hello, world!"
prefix = "Hello"
result = starts_with_using_startswith(string, prefix)
print(f"String '{string}' starts with prefix '{prefix}': {result}")  # Output: String 'Hello, world!' starts with prefix 'Hello': True

# 2. Using Slicing

def starts_with_using_slicing(string, prefix):
    return string[:len(prefix)] == prefix

# Example usage
string = "Hello, world!"
prefix = "Hello"
result = starts_with_using_slicing(string, prefix)
print(f"String '{string}' starts with prefix '{prefix}': {result}")  # Output: String 'Hello, world!' starts with prefix 'Hello': True

# 3. Using re.match()

import re

def starts_with_using_regex(string, prefix):
    return re.match(f"^{re.escape(prefix)}", string) is not None

# Example usage
string = "Hello, world!"
prefix = "Hello"
result = starts_with_using_regex(string, prefix)
print(f"String '{string}' starts with prefix '{prefix}': {result}")  # Output: String 'Hello, world!' starts with prefix 'Hello': True
