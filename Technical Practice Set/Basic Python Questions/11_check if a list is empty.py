# 1. Using len()

def is_empty_len(lst):
    return len(lst) == 0

print(is_empty_len([]))  # Output: True
print(is_empty_len([1, 2, 3]))  # Output: False

# 2. Using Direct Comparison

def is_empty_direct(lst):
    return lst == []

print(is_empty_direct([]))  # Output: True
print(is_empty_direct([1, 2, 3]))  # Output: False

# 3. Using not

def is_empty_not(lst):
    return not lst

print(is_empty_not([]))  # Output: True
print(is_empty_not([1, 2, 3]))  # Output: False

# 4. Using bool()

def is_empty_bool(lst):
    return not bool(lst)

print(is_empty_bool([]))  # Output: True
print(is_empty_bool([1, 2, 3]))  # Output: False
