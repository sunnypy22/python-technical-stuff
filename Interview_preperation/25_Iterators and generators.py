'''
**Iterators** and **generators** are both tools in Python for working with sequences of data.
 They allow you to traverse through data one element at a time without having to
   store the entire dataset in memory.
     However, they operate differently and have distinct characteristics.
'''
### Iterators
'''
**Iterators** are objects that implement the iterator protocol, consisting of 
two main methods:
'''

'''
1. **`__iter__()`**: Returns the iterator object itself. This method is required for an
     object to be an iterator.
2. **`__next__()`**: Returns the next value from the iterator. When there are no more items
     to return, it raises the `StopIteration` exception.
'''

'''
To be an iterator, an object must implement these methods. Iterators are useful when you 
    need to iterate over a sequence but don't need to store the entire sequence in memory.
'''
#### Example of Creating an Iterator

class CountUp:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Usage
count = CountUp(1, 5)
for number in count:
    print(number)
'''
In this example:
- `CountUp` is an iterator that counts from `low` to `high`.
- It implements `__iter__()` and `__next__()` methods.
'''

### Generators
'''
**Generators** provide a convenient way to create iterators using simple functions. 
A generator function uses the `yield` keyword instead of `return`. 
When a generator function is called, it returns a generator object without starting
 execution immediately. When `next()` is called on the generator, execution starts and
   continues until the next `yield` statement is encountered.
'''
#### Characteristics of Generators:

'''
- **Stateful**: Generators maintain their state between calls.
- **Lazy Evaluation**: Values are produced on-the-fly, which can save memory.
- **Simpler Code**: Generators are easier to write and understand compared to 
    traditional iterators.
'''

#### Example of a Generator

def count_up(low, high):
    current = low
    while current <= high:
        yield current
        current += 1

# Usage
for number in count_up(1, 5):
    print(number)

'''
In this example:
- `count_up` is a generator function that yields numbers from `low` to `high`.
- The `yield` keyword is used to produce a sequence of values lazily.
'''

### Differences Between Iterators and Generators

'''
1. **Creation**:
   - **Iterator**: Typically requires creating a class with `__iter__()` and `__next__()` 
    methods.
   - **Generator**: Created using a function with `yield` statements.

2. **Syntax**:
   - **Iterator**: Requires more boilerplate code to implement the iterator protocol.
   - **Generator**: More concise and easier to read, as it uses a function with `yield`.

3. **State Management**:
   - **Iterator**: Manages its own state and needs additional code for this.
   - **Generator**: Automatically manages its state between yields.

4. **Performance**:
   - **Iterator**: May use more memory if the sequence is large or if the state is complex.
   - **Generator**: Efficient in terms of memory, as it produces values one at a time.
'''
### Summary
'''
- **Iterators** are objects that follow the iterator protocol 
    (`__iter__()` and `__next__()`) and are useful for traversing through a sequence of data.
- **Generators** are a simpler way to create iterators using functions with `yield`,
     providing lazy evaluation and better readability.
'''