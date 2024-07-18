# 1. Using String Slicing

def is_palindrome_slice(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome_slice("A man, a plan, a canal, Panama")) 
print(is_palindrome_slice("Hello, World!"))

# 2. Using Iterative Comparison

def is_palindrome_iterative(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome_iterative("A man, a plan, a canal, Panama")) 
print(is_palindrome_iterative("Hello, World!"))  

# 3. Using Recursion

def is_palindrome_recursive(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())

    def helper(left, right):
        if left >= right:
            return True
        if cleaned[left] != cleaned[right]:
            return False
        return helper(left + 1, right - 1)

    return helper(0, len(cleaned) - 1)

print(is_palindrome_recursive("A man, a plan, a canal, Panama")) 
print(is_palindrome_recursive("Hello, World!"))

# 4. Using Two-pointer Technique

def is_palindrome_two_pointer(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome_two_pointer("A man, a plan, a canal, Panama"))  
print(is_palindrome_two_pointer("Hello, World!")) 

# 5. Using Collections (Deque)

from collections import deque

def is_palindrome_deque(s):
    cleaned = deque(char.lower() for char in s if char.isalnum())
    while len(cleaned) > 1:
        if cleaned.popleft() != cleaned.pop():
            return False
    return True


print(is_palindrome_deque("A man, a plan, a canal, Panama"))
print(is_palindrome_deque("Hello, World!"))

# 6. Using Regular Expressions

import re

def is_palindrome_regex(s):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

print(is_palindrome_regex("A man, a plan, a canal, Panama")) 
print(is_palindrome_regex("Hello, World!"))  

# 7. Using Functional Programming (filter and lambda)

def is_palindrome_functional(s):
    cleaned = ''.join(filter(str.isalnum, s)).lower()
    return cleaned == cleaned[::-1]

print(is_palindrome_functional("A man, a plan, a canal, Panama"))  
print(is_palindrome_functional("Hello, World!"))