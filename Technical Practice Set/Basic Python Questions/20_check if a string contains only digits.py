# 1. Using str.isdigit()

def is_digit_string(s):
    return s.isdigit()

# Example usage
input_string = "12345"
print(is_digit_string(input_string))  # Output: True

input_string = "123abc"
print(is_digit_string(input_string))  # Output: False

# 2. Using str.isnumeric()

def is_numeric_string(s):
    return s.isnumeric()

# Example usage
input_string = "12345"
print(is_numeric_string(input_string))  # Output: True

input_string = "123abc"
print(is_numeric_string(input_string))  # Output: False

# 3. Using Regular Expressions

import re

def is_digit_string_regex(s):
    return bool(re.match(r'^\d+$', s))

# Example usage
input_string = "12345"
print(is_digit_string_regex(input_string))  # Output: True

input_string = "123abc"
print(is_digit_string_regex(input_string))  # Output: False
