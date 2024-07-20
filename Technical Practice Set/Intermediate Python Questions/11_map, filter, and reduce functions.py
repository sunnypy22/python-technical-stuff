####### map Function  #######

'''
The map function applies a given function to all items in an iterable (such as a list) 
and returns a map object (an iterator) which can be converted to other
 iterables like lists or tuples.
'''

'''
Syntax:

>> map(function, iterable)

function: The function to apply to each item.
iterable: The iterable to process.
'''

# Example 1: Squaring Numbers

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# Example 2: Converting Strings to Uppercase

strings = ["hello", "world", "python"]
uppercase_strings = map(str.upper, strings)
print(list(uppercase_strings))  # Output: ['HELLO', 'WORLD', 'PYTHON']

######  filter Function     ######

'''
The filter function filters elements from an iterable based on a function that returns
 True or False. It returns a filter object (an iterator) which can
   be converted to other iterables like lists or tuples.
'''

'''
Syntax:

>> filter(function, iterable)

function: The function to test each element.
iterable: The iterable to filter.
'''

# Example 1: Filtering Even Numbers

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

# Example 2: Filtering Non-Empty Strings

strings = ["hello", "", "world", "python", ""]
non_empty_strings = filter(None, strings)
print(list(non_empty_strings))  # Output: ['hello', 'world', 'python']


######      reduce Function     ######


'''
The reduce function applies a binary function (a function that takes two arguments) 
cumulatively to the items of an iterable, from left to right, so as to 
reduce the iterable to a single value. It is available in the functools module.
'''

'''
Syntax:

>> from functools import reduce
>> reduce(function, iterable, [initializer])

function: The function to apply. It takes two arguments.
iterable: The iterable to process.
[initializer]: (Optional) A value to start with. If provided, 
it is the first argument to the function. If not provided, 
the first two items of the iterable are used.
'''

# Example 1: Summing Numbers

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # Output: 15


# Example 2: Finding the Product of Numbers


from functools import reduce

numbers = [1, 2, 3, 4, 5]
product_result = reduce(lambda x, y: x * y, numbers)
print(product_result)  # Output: 120

####    Combining map, filter, and reduce       ####

'''You can combine these functions for more complex data processing tasks.'''

# Example: Processing a List of Numbers

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Step 1: Filter even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Step 2: Square the even numbers
squared_numbers = map(lambda x: x**2, even_numbers)

# Step 3: Sum the squared numbers
result = reduce(lambda x, y: x + y, squared_numbers)

print(result)  # Output: 20 (2^2 + 4^2 = 4 + 16 = 20)

