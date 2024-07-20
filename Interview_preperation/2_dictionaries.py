'''
A dictionary in Python is a collection of key-value pairs,
 where each key is unique and maps to a value. 
Dictionaries are unordered, mutable, and indexed by keys. 
They are one of the most important data structures in Python and 
 are used to store data in a way that allows for quick access and modification
 '''

##### Creating Dictionaries  #####

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Using the dict() function
my_dict = dict(name='Alice', age=30, city='New York')

print(my_dict)


##### Accessing Values  #####

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Using square brackets
print(my_dict['name'])  # Output: Alice

# Using the get() method
print(my_dict.get('age'))  # Output: 30

# Using get() with a default value
print(my_dict.get('country', 'USA'))  # Output: USA


#####  Adding and Updating Values  #####


my_dict = {'name': 'Alice', 'age': 30}

# Adding a new key-value pair
my_dict['city'] = 'New York'

# Updating an existing key-value pair
my_dict['age'] = 31

print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}


####  Removing Key-Value Pairs ####

'''You can remove key-value pairs using the del statement,
 the pop() method, or the popitem() method.
'''

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Using del
del my_dict['age']

# Using pop()
city = my_dict.pop('city')

# Using popitem() to remove the last inserted item (Python 3.7+)
last_item = my_dict.popitem()

print(my_dict)  # Output: {'name': 'Alice'}
print(city)  # Output: New York
print(last_item)  # Output: ('name', 'Alice')


##### Checking for Keys #####

my_dict = {'name': 'Alice', 'age': 30}

# Check if a key exists
print('name' in my_dict)  # Output: True
print('city' in my_dict)  # Output: False


####  Iterating Through a Dictionary  ####

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Iterating through keys
for key in my_dict:
    print(key, my_dict[key])

# Iterating through values
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value)


####### Dictionary Methods #######

'''keys()'''

my_dict = {'name': 'Alice', 'age': 30}
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])


'''values()'''

my_dict = {'name': 'Alice', 'age': 30}
print(my_dict.values())  # Output: dict_values(['Alice', 30])


'''items()'''

my_dict = {'name': 'Alice', 'age': 30}
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 30)])


'''update()'''

my_dict = {'name': 'Alice', 'age': 30}
my_dict.update({'age': 31, 'city': 'New York'})

print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

'''clear()'''

my_dict = {'name': 'Alice', 'age': 30}
my_dict.clear()

print(my_dict)  # Output: {}



#####  Dictionary Comprehensions  #####

# Creating a dictionary with squares of numbers
squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filtering items
even_squares = {x: x*x for x in range(1, 6) if x % 2 == 0}
print(even_squares)  # Output: {2: 4, 4: 16}

