'''In Python, you can use the zip() function to combine multiple iterables (such as lists, tuples, or strings)
into a single iterator of tuples. Each tuple contains elements from the corresponding position in each iterable.
Here's a basic overview and some examples of how to use the zip() function
'''

### Combining Two Lists:

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

### Combining Multiple Lists:

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]

zipped = zip(list1, list2, list3)
print(list(zipped))  # Output: [(1, 'a', True), (2, 'b', False), (3, 'c', True)]

### Handling Different Lengths:

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

'''Using zip() with a Loop
'''

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for num, char in zip(list1, list2):
    print(f'Number: {num}, Character: {char}')

### Unzipping

'''To unzip a list of tuples, you can use the zip() function with the unpacking operator *:
'''

zipped = [(1, 'a'), (2, 'b'), (3, 'c')]

numbers, characters = zip(*zipped)
print(numbers)     # Output: (1, 2, 3)
print(characters)  # Output: ('a', 'b', 'c')

'''The zip() function is very useful for pairing elements from multiple iterables.
It's commonly used in situations where you need to process corresponding elements
from multiple sequences together.'''
