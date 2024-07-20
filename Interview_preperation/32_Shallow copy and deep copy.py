'''In Python, copying objects is crucial for creating duplicates of data structures
 while ensuring that changes to one copy do not unintentionally affect the other. 
 Shallow copy and deep copy are two ways to achieve this, each with different 
 implications for how data is copied.
'''

### Shallow Copy
'''
**Definition**: A shallow copy creates a new object but does not create copies
     of the objects contained within the original object. Instead, it copies references
       to the objects. This means that changes to the mutable objects within the original
         and the copied object will affect both objects.
'''

'''
**How to Create**:
1. **Using the `copy` Module**:
   import copy
   shallow_copy = copy.copy(original)

2. **Using Object's Built-in Methods**:
   - For lists: `new_list = old_list.copy()`
   - For dictionaries: `new_dict = old_dict.copy()`
'''

# **Example**:
import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original)

# Modify an element in the inner list
shallow_copy[0][0] = 10

print("Original:", original)       # Output: Original: [[10, 2, 3], [4, 5, 6]]
print("Shallow Copy:", shallow_copy)  # Output: Shallow Copy: [[10, 2, 3], [4, 5, 6]]
'''
**Key Points**:
- **Reference Copy**: Only the outer object is copied; inner objects 
    (lists, dictionaries) are shared between the original and the copy.
- **Use Case**: Suitable when you need a copy of the outer structure but the inner
     contents remain the same.
'''

### Deep Copy
'''
**Definition**: A deep copy creates a new object and recursively copies all objects 
    found within the original object. This means that the new object is completely
      independent of the original, and changes to the original do not affect the deep copy,
        and vice versa.
'''

'''
**How to Create**:
1. **Using the `copy` Module**:
   import copy
   deep_copy = copy.deepcopy(original)
'''

# **Example**:
import copy

original = [[1, 2, 3], [4, 5, 6]]
deep_copy = copy.deepcopy(original)

# Modify an element in the inner list
deep_copy[0][0] = 10

print("Original:", original)       # Output: Original: [[1, 2, 3], [4, 5, 6]]
print("Deep Copy:", deep_copy)     # Output: Deep Copy: [[10, 2, 3], [4, 5, 6]]

'''
**Key Points**:
- **Recursive Copy**: Both the outer and all inner objects are copied, so the original 
    and copy are completely independent.
- **Use Case**: Suitable when you need a full duplicate of an object and its contents, 
    including nested objects.
'''
### Summary

'''
- **Shallow Copy**:
  - Copies the outer object and references to inner objects.
  - Changes to mutable inner objects affect both the original and the copy.
  - Created using `copy.copy()` or built-in methods like `list.copy()`.

- **Deep Copy**:
  - Recursively copies the outer object and all nested objects.
  - The original and the copy are fully independent.
  - Created using `copy.deepcopy()`.
'''