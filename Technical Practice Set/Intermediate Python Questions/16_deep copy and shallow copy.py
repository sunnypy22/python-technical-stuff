#### Shallow Copy   ####

'''A shallow copy of an object creates a new object, but inserts references into it to
 the objects found in the original. 
This means that only the top-level objects are duplicated, while nested objects are not.'''


# 1. Using the copy module

import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = copy.copy(original)

print(shallow_copied)  # Output: [[1, 2, 3], [4, 5, 6]]

shallow_copied[0][0] = 'X'
print(original)  # Output: [['X', 2, 3], [4, 5, 6]]

# 2. Using List Slicing

original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = original[:]

print(shallow_copied)  # Output: [[1, 2, 3], [4, 5, 6]]

shallow_copied[0][0] = 'X'
print(original)  # Output: [['X', 2, 3], [4, 5, 6]]

# 3. Using the copy method for lists

original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = original.copy()

print(shallow_copied)  # Output: [[1, 2, 3], [4, 5, 6]]

shallow_copied[0][0] = 'X'
print(original)  # Output: [['X', 2, 3], [4, 5, 6]]


####    Deep Copy   ####

'''A deep copy creates a new object and recursively adds copies of nested objects 
found in the original.
 This means that all objects are duplicated, not just the top-level ones.'''

# 1. Using the copy module

import copy

original = [[1, 2, 3], [4, 5, 6]]
deep_copied = copy.deepcopy(original)

print(deep_copied)  # Output: [[1, 2, 3], [4, 5, 6]]

deep_copied[0][0] = 'X'
print(original)  # Output: [[1, 2, 3], [4, 5, 6]]

'''
Differences
Level of Copy:

Shallow Copy: Only copies the top-level object. Nested objects are not copied, but their references are included.
Deep Copy: Recursively copies all objects, including nested objects.
Memory Usage:

Shallow Copy: Generally uses less memory because it doesn’t create copies of nested objects.
Deep Copy: Uses more memory as it creates a complete duplicate of the original object, including all nested objects.
Modification Impact:

Shallow Copy: Modifications to nested objects in the copied object reflect in the original object.
Deep Copy: Modifications to nested objects in the copied object do not affect the original object.

'''

# 1. Shallow Copy Example

original = {'a': [1, 2, 3], 'b': [4, 5, 6]}
shallow_copied = copy.copy(original)

print(shallow_copied)  # Output: {'a': [1, 2, 3], 'b': [4, 5, 6]}

shallow_copied['a'][0] = 'X'
print(original)  # Output: {'a': ['X', 2, 3], 'b': [4, 5, 6]}

# 2. Deep Copy Example

original = {'a': [1, 2, 3], 'b': [4, 5, 6]}
deep_copied = copy.deepcopy(original)

print(deep_copied)  # Output: {'a': [1, 2, 3], 'b': [4, 5, 6]}

deep_copied['a'][0] = 'X'
print(original)  # Output: {'a': [1, 2, 3], 'b': [4, 5, 6]}

# 1. Using List Comprehension for Shallow Copy

original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = [item for item in original]

print(shallow_copied)  # Output: [[1, 2, 3], [4, 5, 6]]

shallow_copied[0][0] = 'X'
print(original)  # Output: [['X', 2, 3], [4, 5, 6]]

# 2. Using JSON Serialization for Deep Copy

import json

original = {'a': [1, 2, 3], 'b': [4, 5, 6]}
deep_copied = json.loads(json.dumps(original))

print(deep_copied)  # Output: {'a': [1, 2, 3], 'b': [4, 5, 6]}

deep_copied['a'][0] = 'X'
print(original)  # Output: {'a': [1, 2, 3], 'b': [4, 5, 6]}