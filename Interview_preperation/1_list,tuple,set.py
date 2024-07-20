'''
In Python, lists, tuples, and sets are all used to store collections of items, 
but they have distinct characteristics and use cases.
'''
######  List    ######

'''

1. Mutable: Lists are mutable, meaning you can change their contents
         (add, remove, or modify elements) after they are created.
2. Ordered: Lists maintain the order of elements as they are inserted.
3. Indexed: Elements in a list can be accessed by their index.
4. Allows Duplicates: Lists can contain duplicate elements.
5. Syntax: Defined using square brackets `[]`.

'''

# Example


my_list = [1, 2, 3, 4]
print(my_list)  # Output: [1, 2, 3, 4]

my_list.append(5)
print(my_list)  # Output: [1, 2, 3, 4, 5]

my_list[2] = 10
print(my_list)  # Output: [1, 2, 10, 4, 5]


######  Tuple   ######

'''

1. Immutable: Tuples are immutable, meaning once they are created, 
        their contents cannot be changed.
2. Ordered: Tuples maintain the order of elements as they are inserted.
3. Indexed: Elements in a tuple can be accessed by their index.
4. Allows Duplicates: Tuples can contain duplicate elements.
5. Syntax: Defined using parentheses `()`.

'''

# Example

my_tuple = (1, 2, 3, 4)
print(my_tuple)  # Output: (1, 2, 3, 4)

# my_tuple.append(5)  # This will raise an AttributeError
# my_tuple[2] = 10    # This will raise a TypeError

# Tuples are often used for data that should not change
person = ("Alice", 30)
print(person)  # Output: ("Alice", 30)

######  Set ######

'''
1. Mutable: Sets are mutable, meaning you can change their contents 
        (add or remove elements) after they are created. However, the elements themselves must be immutable.
2. Unordered: Sets do not maintain the order of elements.
3. Unindexed: Elements in a set cannot be accessed by an index.
4. No Duplicates: Sets do not allow duplicate elements. Each element is unique.
5. Syntax: Defined using curly braces `{}` or the `set()` function.

'''

# Example

my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5}

# Adding a duplicate element has no effect
my_set.add(2)
print(my_set)  # Output: {1, 2, 4, 5}

# Summary of Differences

'''

| Feature           | List           | Tuple          | Set            |
|-------------------|----------------|----------------|----------------|
| Mutability        | Mutable        | Immutable      | Mutable        |
| Order             | Ordered        | Ordered        | Unordered      |
| Indexing          | Indexed        | Indexed        | Unindexed      |
| Duplicates        | Allows         | Allows         | No Duplicates  |
| Syntax            | `[]`           | `()`           | `{}` or `set()`|

'''

### Use Cases

'''

- List: Use lists when you need a collection of items that may change, 
    and the order of items is important.
- Tuple: Use tuples when you need a collection of items that should not
    change and where the order is important.
- Set: Use sets when you need a collection of unique items and the order 
    of items is not important.

'''