'''The `itertools` module in Python provides a collection of fast, 
memory-efficient tools for handling iterators. 
These functions help in creating iterators for efficient looping, 
which is especially useful when dealing with large datasets. 
'''
### Commonly Used Functions

'''
1. **`count`**
2. **`cycle`**
3. **`repeat`**
4. **`accumulate`**
5. **`chain`**
6. **`compress`**
7. **`dropwhile`**
8. **`takewhile`**
9. **`filterfalse`**
10. **`islice`**
11. **`starmap`**
12. **`tee`**
13. **`product`**
14. **`permutations`**
15. **`combinations`**
16. **`combinations_with_replacement`**
17. **`groupby`**
'''

### Examples

#### `count`
'''
Creates an iterator that generates consecutive integers, starting from a specified number.
'''
from itertools import count

for i in count(10):
    if i > 15:
        break
    print(i)
# Output: 10 11 12 13 14 15

#### `cycle`
'''
Creates an iterator that cycles through the elements of an iterable indefinitely.
'''

from itertools import cycle

counter = 0
for item in cycle('ABC'):
    if counter == 6:
        break
    print(item)
    counter += 1
# Output: A B C A B C

#### `repeat`

'''
Creates an iterator that repeats an object a specified number of times.
'''

from itertools import repeat

for item in repeat('Hello', 3):
    print(item)
# Output: Hello Hello Hello

#### `accumulate`
'''
Creates an iterator that returns accumulated sums or accumulated results of other binary functions.
'''

from itertools import accumulate

numbers = [1, 2, 3, 4]
accumulated = accumulate(numbers)
print(list(accumulated))
# Output: [1, 3, 6, 10]

#### `chain`
'''
Creates an iterator that returns elements from the first iterable until it is exhausted, then proceeds to the next iterable.
'''

from itertools import chain

a = [1, 2, 3]
b = [4, 5, 6]
chained = chain(a, b)
print(list(chained))
# Output: [1, 2, 3, 4, 5, 6]

#### `compress`
'''
Filters elements from an iterable based on a selector iterable.
'''

from itertools import compress

data = 'ABCDE'
selectors = [1, 0, 1, 0, 1]
compressed = compress(data, selectors)
print(list(compressed))
# Output: ['A', 'C', 'E']

#### `dropwhile`
'''
Creates an iterator that drops elements from the iterable as long as the predicate is true; 
afterwards, returns every remaining element.
'''

from itertools import dropwhile

numbers = [1, 2, 3, 4, 5, 6]
dropped = dropwhile(lambda x: x < 4, numbers)
print(list(dropped))
# Output: [4, 5, 6]

#### `takewhile`

'''
Creates an iterator that returns elements from the iterable as long as the predicate is true.
'''
from itertools import takewhile

numbers = [1, 2, 3, 4, 5, 6]
taken = takewhile(lambda x: x < 4, numbers)
print(list(taken))
# Output: [1, 2, 3]

#### `filterfalse`

'''
Creates an iterator that filters elements from an iterable, returning only those for which the predicate is false.
'''

from itertools import filterfalse

numbers = [1, 2, 3, 4, 5, 6]
filtered = filterfalse(lambda x: x % 2 == 0, numbers)
print(list(filtered))
# Output: [1, 3, 5]

#### `islice`
'''
Creates an iterator that returns selected elements from the iterable.
'''

from itertools import islice

numbers = [1, 2, 3, 4, 5, 6]
sliced = islice(numbers, 2, 5)
print(list(sliced))
# Output: [3, 4, 5]

#### `starmap`
'''
Creates an iterator that computes the function using arguments obtained from the iterable.
'''
from itertools import starmap

pairs = [(1, 2), (3, 4), (5, 6)]
result = starmap(lambda x, y: x * y, pairs)
print(list(result))
# Output: [2, 12, 30]

#### `tee`
'''
Creates multiple independent iterators from a single iterable.
'''
from itertools import tee

numbers = [1, 2, 3, 4]
iter1, iter2 = tee(numbers, 2)
print(list(iter1))  # Output: [1, 2, 3, 4]
print(list(iter2))  # Output: [1, 2, 3, 4]

#### `product`
'''
Creates an iterator that returns Cartesian product of input iterables.
'''
from itertools import product

result = product('AB', repeat=2)
print(list(result))
# Output: [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]

#### `permutations`
'''
Creates an iterator that returns all possible permutations of the input iterable.
'''
from itertools import permutations

result = permutations('ABC', 2)
print(list(result))
# Output: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

#### `combinations`
'''
Creates an iterator that returns all possible combinations of the input iterable.
'''
from itertools import combinations

result = combinations('ABC', 2)
print(list(result))
# Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]

#### `combinations_with_replacement`
'''
Creates an iterator that returns all possible combinations of the input iterable, allowing individual elements to be repeated more than once.
'''
from itertools import combinations_with_replacement

result = combinations_with_replacement('ABC', 2)
print(list(result))
# Output: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

#### `groupby`
'''
Creates an iterator that returns consecutive keys and groups from the input iterable.
'''
from itertools import groupby

data = 'AAAABBBCCDAA'
grouped = groupby(data)

for key, group in grouped:
    print(key, list(group))
# Output:
# A ['A', 'A', 'A', 'A']
# B ['B', 'B', 'B']
# C ['C', 'C']
# D ['D']
# A ['A', 'A']