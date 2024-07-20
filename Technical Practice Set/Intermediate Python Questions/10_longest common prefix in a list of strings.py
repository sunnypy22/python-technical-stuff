# Method 1: Horizontal Scanning

'''This method compares characters of each string one by one.'''

def longest_common_prefix_horizontal(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for s in strings[1:]:
        while s.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Example usage
strings = ["flower", "flow", "flight"]
print("Longest Common Prefix (Horizontal Scanning):", longest_common_prefix_horizontal(strings))  # Output: "fl"

# Method 2: Vertical Scanning

'''This method compares characters at each position of the strings one by one.'''

def longest_common_prefix_vertical(strings):
    if not strings:
        return ""
    for i in range(len(strings[0])):
        char = strings[0][i]
        for s in strings[1:]:
            if i >= len(s) or s[i] != char:
                return strings[0][:i]
    return strings[0]

# Example usage
strings = ["flower", "flow", "flight"]
print("Longest Common Prefix (Vertical Scanning):", longest_common_prefix_vertical(strings))  # Output: "fl"

# Method 3: Divide and Conquer

'''This method divides the list of strings into two halves and
 finds the common prefix in each half.'''

def common_prefix(left, right):
    min_length = min(len(left), len(right))
    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]
    return left[:min_length]

def longest_common_prefix_divide_and_conquer(strings):
    if not strings:
        return ""
    
    def longest_common_prefix_rec(strings, left, right):
        if left == right:
            return strings[left]
        else:
            mid = (left + right) // 2
            lcp_left = longest_common_prefix_rec(strings, left, mid)
            lcp_right = longest_common_prefix_rec(strings, mid + 1, right)
            return common_prefix(lcp_left, lcp_right)
    
    return longest_common_prefix_rec(strings, 0, len(strings) - 1)

# Example usage
strings = ["flower", "flow", "flight"]
print("Longest Common Prefix (Divide and Conquer):", longest_common_prefix_divide_and_conquer(strings))  # Output: "fl"

# Method 4: Binary Search

'''This method uses binary search to find the common prefix.'''

def is_common_prefix(strings, length):
    str1 = strings[0][:length]
    for s in strings:
        if not s.startswith(str1):
            return False
    return True

def longest_common_prefix_binary_search(strings):
    if not strings:
        return ""
    min_len = min(len(s) for s in strings)
    low, high = 0, min_len
    while low <= high:
        mid = (low + high) // 2
        if is_common_prefix(strings, mid):
            low = mid + 1
        else:
            high = mid - 1
    return strings[0][:(low + high) // 2]

# Example usage
strings = ["flower", "flow", "flight"]
print("Longest Common Prefix (Binary Search):", longest_common_prefix_binary_search(strings))  # Output: "fl"


# Method 5: Using zip and itertools.takewhile

'''This method uses zip to pair the 
characters from each string and itertools.takewhile to find the common prefix.'''

from itertools import takewhile

def longest_common_prefix_zip(strings):
    if not strings:
        return ""
    # Use zip to pair characters and takewhile to find common prefix
    common = "".join(c[0] for c in takewhile(lambda x: all(x[0] == y for y in x), zip(*strings)))
    return common

# Example usage
strings = ["flower", "flow", "flight"]
print("Longest Common Prefix (zip and takewhile):", longest_common_prefix_zip(strings))  # Output: "fl"
