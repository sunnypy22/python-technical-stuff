'''Functional programming (FP) is a programming paradigm that treats computation as the 
    evaluation of mathematical functions and avoids changing state or mutable data. 
    This paradigm is characterized by the use of pure functions, higher-order functions,
      and immutability. Python supports functional programming features and paradigms, 
      although it is not purely a functional programming language.
'''

### Key Concepts of Functional Programming
'''
1. **Pure Functions**:
   - **Definition**: A function is considered pure if it produces the same output for 
    the same input and does not cause any side effects (e.g., modifying global state).
   - **Example**:
     def add(x, y):
         return x + y

2. **Immutability**:
   - **Definition**: In functional programming, data structures are immutable, meaning 
    once created, they cannot be changed.
   - **Example**:
     # Immutable tuple
     tup = (1, 2, 3)
     # tup[0] = 4  # This will raise an error

3. **Higher-Order Functions**:
   - **Definition**: Functions that take other functions as arguments or return functions
         as results.
   - **Example**:
     def apply_func(func, value):
         return func(value)

     def square(x):
         return x * x

     print(apply_func(square, 4))  # Output: 16

4. **First-Class Functions**:
   - **Definition**: Functions that can be passed as arguments, returned from other
         functions, and assigned to variables.
   - **Example**:
     def make_multiplier(n):
         def multiplier(x):
             return x * n
         return multiplier

     double = make_multiplier(2)
     print(double(5))  # Output: 10

5. **Function Composition**:
   - **Definition**: Combining two or more functions to create a new function.
   - **Example**:
     def square(x):
         return x * x

     def increment(x):
         return x + 1

     def composed_function(x):
         return increment(square(x))

     print(composed_function(3))  # Output: 10

6. **Map, Filter, and Reduce**:
   - **Map**: Applies a function to all items in an iterable and returns a list of results.
     numbers = [1, 2, 3, 4]
     squares = map(lambda x: x * x, numbers)
     print(list(squares))  # Output: [1, 4, 9, 16]
   - **Filter**: Filters items in an iterable based on a function that returns a boolean.
     numbers = [1, 2, 3, 4, 5]
     evens = filter(lambda x: x % 2 == 0, numbers)
     print(list(evens))  # Output: [2, 4]
   - **Reduce**: Applies a function cumulatively to items in an iterable, 
    from left to right, to reduce it to a single value.
     from functools import reduce

     numbers = [1, 2, 3, 4]
     product = reduce(lambda x, y: x * y, numbers)
     print(product)  # Output: 24
'''

### Advantages of Functional Programming
'''
1. **Modularity**: Functions can be easily reused and composed.
2. **Readability**: Pure functions and immutability make code easier to reason about.
3. **Testability**: Pure functions are easier to test due to their predictable behavior.
4. **Concurrency**: Immutability and stateless functions make it easier to write 
concurrent and parallel programs.
'''
### Functional Programming in Python
'''
Python is a multi-paradigm language that supports functional programming alongside
 object-oriented and imperative programming. Here are some functional programming 
 features available in Python:

- **Lambda Functions**: Anonymous functions defined using the `lambda` keyword.
  add = lambda x, y: x + y
  print(add(5, 3))  # Output: 8

- **List Comprehensions**: Compact way to create lists.
  numbers = [1, 2, 3, 4, 5]
  squares = [x * x for x in numbers]
  print(squares)  # Output: [1, 4, 9, 16, 25]

- **Generator Expressions**: Similar to list comprehensions but return a generator object.
  numbers = [1, 2, 3, 4, 5]
  squares = (x * x for x in numbers)
  print(list(squares))  # Output: [1, 4, 9, 16, 25]

'''