# Method 1: Using Sorting

def are_anagrams_sorting(str1, str2):
    return sorted(str1) == sorted(str2)

# Example usage
str1 = "listen"
str2 = "silent"
print(are_anagrams_sorting(str1, str2))  # Output: True

# Method 2: Using a Counter (from the collections module)

from collections import Counter

def are_anagrams_counter(str1, str2):
    return Counter(str1) == Counter(str2)

# Example usage
str1 = "listen"
str2 = "silent"
print(are_anagrams_counter(str1, str2))  # Output: True

# Method 3: Using Dictionary Counting

def are_anagrams_dict_counting(str1, str2):
    if len(str1) != len(str2):
        return False

    count1 = {}
    count2 = {}

    for char in str1:
        count1[char] = count1.get(char, 0) + 1
    for char in str2:
        count2[char] = count2.get(char, 0) + 1

    return count1 == count2

# Example usage
str1 = "listen"
str2 = "silent"
print(are_anagrams_dict_counting(str1, str2))  # Output: True

# Method 4: Using Set Operations


def are_anagrams_set_operations(str1, str2):
    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)

# Example usage
str1 = "listen"
str2 = "silent"
print(are_anagrams_set_operations(str1, str2))  # Output: True

# Method 5: Using Character Frequency Array

def are_anagrams_frequency_array(str1, str2):
    if len(str1) != len(str2):
        return False

    # Assuming the strings are lowercase letters only
    count = [0] * 26  # For 26 letters in the English alphabet

    for char in str1:
        count[ord(char) - ord('a')] += 1
    for char in str2:
        count[ord(char) - ord('a')] -= 1

    return all(x == 0 for x in count)

# Example usage
str1 = "listen"
str2 = "silent"
print(are_anagrams_frequency_array(str1, str2))  # Output: True

# Method 6: Using Python’s collections.defaultdict

from collections import defaultdict

def are_anagrams_defaultdict(str1, str2):
    if len(str1) != len(str2):
        return False

    count1 = defaultdict(int)
    count2 = defaultdict(int)

    for char in str1:
        count1[char] += 1
    for char in str2:
        count2[char] += 1

    return count1 == count2

# Example usage
str1 = "listen"
str2 = "silent"
print(are_anagrams_defaultdict(str1, str2))  # Output: True

# Method 7: Using Bit Manipulation (for fixed-size character sets)

def are_anagrams_bitwise(str1, str2):
    if len(str1) != len(str2):
        return False

    bit_vector1 = 0
    bit_vector2 = 0

    for char in str1:
        bit_vector1 ^= 1 << (ord(char) - ord('a'))
    for char in str2:
        bit_vector2 ^= 1 << (ord(char) - ord('a'))

    return bit_vector1 == bit_vector2

# Example usage
str1 = "listen"
str2 = "silent"
print(are_anagrams_bitwise(str1, str2))  # Output: True

# Method 8: Using Regular Expressions (for sanitized inputs)

import re
from collections import Counter

def are_anagrams_regex(str1, str2):
    # Remove non-alphanumeric characters and convert to lowercase
    sanitized_str1 = re.sub(r'[^a-zA-Z]', '', str1).lower()
    sanitized_str2 = re.sub(r'[^a-zA-Z]', '', str2).lower()

    return Counter(sanitized_str1) == Counter(sanitized_str2)

# Example usage
str1 = "Listen!"
str2 = "Silent@"
print(are_anagrams_regex(str1, str2))  # Output: True
