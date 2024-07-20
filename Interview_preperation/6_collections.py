'''In Python, the `collections` module provides alternatives to Python’s
 general-purpose built-in containers like `dict`, `list`, `set`, and `tuple`. 
 These specialized container data types provide additional 
 functionality, better performance, and more readability for specific use cases.
'''
### Types of Collections

'''
1. **namedtuple**
2. **deque**
3. **ChainMap**
4. **Counter**
5. **OrderedDict**
6. **defaultdict**
'''

# Let's explore each of these with examples:

### 1. namedtuple

'''
`namedtuple` is a factory function for creating tuple subclasses with named fields. It makes the code more readable by accessing elements through named attributes instead of index positions.
'''

from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance of Point
p = Point(11, 22)

# Access elements
print(p.x)  # Output: 11
print(p.y)  # Output: 22

# Access by index
print(p[0])  # Output: 11
print(p[1])  # Output: 22

### 2. deque

'''
`deque` (double-ended queue) is a list-like container with fast appends and pops from both ends.
'''

from collections import deque

# Create a deque
d = deque(['a', 'b', 'c'])

# Append to the right
d.append('d')
print(d)  # Output: deque(['a', 'b', 'c', 'd'])

# Append to the left
d.appendleft('z')
print(d)  # Output: deque(['z', 'a', 'b', 'c', 'd'])

# Pop from the right
d.pop()
print(d)  # Output: deque(['z', 'a', 'b', 'c'])

# Pop from the left
d.popleft()
print(d)  # Output: deque(['a', 'b', 'c'])

### 3. ChainMap

'''
`ChainMap` groups multiple dictionaries into a single, updateable view.
'''

from collections import ChainMap

# Create dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Create a ChainMap
chain = ChainMap(dict1, dict2)

print(chain)  # Output: ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
print(chain['a'])  # Output: 1
print(chain['b'])  # Output: 2 (value from the first dictionary)
print(chain['c'])  # Output: 4

### 4. Counter

'''
`Counter` is a dict subclass for counting hashable objects. 
It’s a collection where elements are stored as dictionary keys, and
 their counts are stored as dictionary values.
'''

from collections import Counter

# Create a Counter
c = Counter(['a', 'b', 'c', 'a', 'b', 'b'])

print(c)  # Output: Counter({'b': 3, 'a': 2, 'c': 1})

# Access count
print(c['a'])  # Output: 2
print(c['b'])  # Output: 3

# Add counts
c.update(['a', 'b', 'b', 'c'])
print(c)  # Output: Counter({'b': 5, 'a': 3, 'c': 2})

### 5. OrderedDict

'''
`OrderedDict` is a dict subclass that remembers the order in which items were inserted.
'''

from collections import OrderedDict

# Create an OrderedDict
od = OrderedDict()

# Insert items
od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Order is maintained
for key in od:
    print(key, od[key])

### 6. defaultdict

'''
`defaultdict` is a dict subclass that calls a factory function to supply missing values.
'''

from collections import defaultdict

# Create a defaultdict with list as the default factory
dd = defaultdict(list)

# Access a missing key returns an empty list
print(dd['a'])  # Output: []

# Append to the list
dd['a'].append(1)
dd['a'].append(2)

print(dd)  # Output: defaultdict(<class 'list'>, {'a': [1, 2]})

# Create a defaultdict with int as the default factory
dd = defaultdict(int)

# Access a missing key returns 0
print(dd['a'])  # Output: 0

# Increment the count
dd['a'] += 1
dd['a'] += 2

print(dd)  # Output: defaultdict(<class 'int'>, {'a': 3})

### Summary

'''
The `collections` module provides specialized container datatypes that improve 
the performance and readability of your code. Here is a quick overview of their use cases:
'''

'''
- `namedtuple`: Access tuple elements using named attributes.
- `deque`: Efficiently append and pop items from both ends.
- `ChainMap`: Combine multiple dictionaries into a single view.
- `Counter`: Count occurrences of elements.
- `OrderedDict`: Maintain insertion order of dictionary items.
- `defaultdict`: Automatically handle missing keys with default values.
'''