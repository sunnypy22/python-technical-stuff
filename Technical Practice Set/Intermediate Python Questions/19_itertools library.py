'''The itertools library in Python is a powerful module that provides various 
functions that work on iterators to produce complex iterators.
 This library is particularly useful for creating efficient and fast looping constructs.
 Here are some of the key
 functions provided by the itertools library along with examples of how to use them:
'''

# 1. Infinite Iterators


'''count()
Generates consecutive integers starting from a specified number.'''

import itertools

for i in itertools.count(start=5, step=2):
    if i > 15:
        break
    print(i)  # Output: 5, 7, 9, 11, 13, 15

'''cycle()
Cycles through an iterable indefinitely.
'''

import itertools

count = 0
for item in itertools.cycle(['A', 'B', 'C']):
    if count > 6:
        break
    print(item)  # Output: A, B, C, A, B, C, A
    count += 1

'''repeat()
Repeats an object a specified number of times. If the number of repetitions is not specified, 
it will repeat indefinitely.
'''

import itertools

for item in itertools.repeat('Hello', 3):
    print(item)  # Output: Hello, Hello, Hello


# 2. Finite Iterators

'''chain()
Combines multiple iterables into a single iterator.
'''

import itertools

for item in itertools.chain([1, 2, 3], ['a', 'b', 'c']):
    print(item)  # Output: 1, 2, 3, a, b, c

'''compress()
Filters elements in an iterable based on the corresponding elements in a selector iterable.
'''

import itertools

data = ['A', 'B', 'C', 'D']
selectors = [1, 0, 1, 0]

for item in itertools.compress(data, selectors):
    print(item)  # Output: A, C

'''dropwhile()
Drops elements from an iterable as long as the predicate is true; once the predicate becomes false,
 returns every remaining element.
'''

import itertools

for item in itertools.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]):
    print(item)  # Output: 6, 4, 1

'''takewhile()
Returns elements from an iterable as long as the predicate is true.
'''

import itertools

for item in itertools.takewhile(lambda x: x < 5, [1, 4, 6, 4, 1]):
    print(item)  # Output: 1, 4

# 3. Combinatoric Iterators

'''product()
Returns the Cartesian product of input iterables.
'''

import itertools

for item in itertools.product([1, 2], ['a', 'b']):
    print(item)  # Output: (1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')

'''permutations()
Generates all possible permutations of an iterable.
'''

import itertools

for item in itertools.permutations([1, 2, 3], 2):
    print(item)  # Output: (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)

'''combinations()
Generates all possible combinations of an iterable.
'''

import itertools

for item in itertools.combinations([1, 2, 3], 2):
    print(item)  # Output: (1, 2), (1, 3), (2, 3)

'''combinations_with_replacement()
Generates all possible combinations of an iterable, allowing for repeated elements.
'''

import itertools

for item in itertools.combinations_with_replacement([1, 2], 2):
    print(item)  # Output: (1, 1), (1, 2), (2, 2)

# 4. Other Useful Functions

'''accumulate()
Makes an iterator that returns accumulated sums, or the result of other binary functions 
(specified via the optional func argument).
'''

import itertools
import operator

data = [1, 2, 3, 4, 5]

# Default: sum
for item in itertools.accumulate(data):
    print(item)  # Output: 1, 3, 6, 10, 15

# Using operator.mul
for item in itertools.accumulate(data, operator.mul):
    print(item)  # Output: 1, 2, 6, 24, 120

'''groupby()
Groups adjacent elements in an iterable based on a specified key function.
'''

import itertools

data = [{'name': 'A', 'age': 20}, {'name': 'B', 'age': 20}, {'name': 'C', 'age': 21}]

# Group by age
for key, group in itertools.groupby(data, key=lambda x: x['age']):
    print(key, list(group))  
    # Output:
    # 20 [{'name': 'A', 'age': 20}, {'name': 'B', 'age': 20}]
    # 21 [{'name': 'C', 'age': 21}]
