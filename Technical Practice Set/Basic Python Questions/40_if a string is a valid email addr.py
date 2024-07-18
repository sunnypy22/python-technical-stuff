# 1. Using Regular Expressions (Regex)

'''Regular expressions provide a flexible and powerful way to validate email
 addresses based on patterns. Here's a basic example using regex to check for a valid email format:'''

import re

def is_valid_email_regex(email):
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Example usage
email1 = "example@example.com"
email2 = "invalid.email"
email3 = "user@subdomain.domain.com"

print(f"Is '{email1}' a valid email? {is_valid_email_regex(email1)}")  # True
print(f"Is '{email2}' a valid email? {is_valid_email_regex(email2)}")  # False
print(f"Is '{email3}' a valid email? {is_valid_email_regex(email3)}")  # True

# 2. Using validate_email from validate_email Library

'''You can install the validate_email library (pip install validate_email) and use its validate_email 
function to check if a string is a valid email address according to various validation checks, 
including format and domain existence.
'''

from validate_email import validate_email

def is_valid_email_library(email):
    return validate_email(email)

# Example usage
email1 = "example@example.com"
email2 = "invalid.email"
email3 = "user@subdomain.domain.com"

print(f"Is '{email1}' a valid email? {is_valid_email_library(email1)}")  # True
print(f"Is '{email2}' a valid email? {is_valid_email_library(email2)}")  # False
print(f"Is '{email3}' a valid email? {is_valid_email_library(email3)}")  # True
