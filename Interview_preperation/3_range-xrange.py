'''In Python, `range` and `xrange` were used to generate sequences of numbers. 
    However, there is an important distinction between them:
'''

'''
1. `range`: Used in both Python 2 and Python 3, but behaves differently.
2. `xrange`: Available only in Python 2.

'''

### `range` in Python 2

'''
In Python 2, `range` returns a list.
'''

# Python 2 example
numbers = range(5)
print(numbers)  # Output: [0, 1, 2, 3, 4]

### `xrange` in Python 2

'''
In Python 2, `xrange` returns an `xrange` object, which is a generator and
 produces numbers on demand (lazy evaluation).
'''

'''
numbers = xrange(5)
print(numbers)  # Output: xrange(0, 5)
'''

for num in numbers:
    print(num)  # Output: 0 1 2 3 4

### `range` in Python 3

'''
In Python 3, `range` behaves like `xrange` in Python 2, returning a range object which
 is an immutable sequence type.
'''
# Python 3 example
numbers = range(5)
print(numbers)  # Output: range(0, 5)

for num in numbers:
    print(num)  # Output: 0 1 2 3 4

print(list(numbers))  # Output: [0, 1, 2, 3, 4]

### Key Differences and Usage

#### Memory Efficiency

'''
- `range` in Python 2 creates a list and stores all the values in memory. 
    This can be memory inefficient for large ranges.
- `xrange` in Python 2 and `range` in Python 3 generate values on the fly and
     are more memory efficient.
'''

#### Iteration

'''
Both `xrange` in Python 2 and `range` in Python 3 are used to iterate over a sequence of
     numbers without generating the entire list at once, which is useful for large ranges.
'''

#### Performance

'''
`xrange` in Python 2 and `range` in Python 3 provide better performance when iterating over 
large sequences since they do not generate all elements at once.
'''

### Example Comparison

'''
Here's a comparison of `range` and `xrange` in Python 2, and `range` in Python 3:
'''

# Python 2 code
# Using range
for i in range(1000000):
    pass  # Do something with i

'''
for i in xrange(1000000): # Using xrange
    pass  # Do something with i
'''


# Python 3 code
# Using range
for i in range(1000000):
    pass  # Do something with i

### Summary

'''
- **Python 2**:
  - `range`: Returns a list.
  - `xrange`: Returns an xrange object (generator).
- **Python 3**:
  - `range`: Behaves like `xrange` in Python 2, returning a range object (generator-like).
'''