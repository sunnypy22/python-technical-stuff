'''
Strings in Python are sequences of characters used to store and manipulate text. 
They are one of the most commonly used data types and offer a wide range of functionalities.
'''

#### Creating Strings  ####

'''Strings can be created using single quotes, double quotes, or triple quotes.'''

single_quote_str = 'Hello, World!'

double_quote_str = "Hello, World!"

triple_quote_str = """This is a
multi-line string."""

#### Accessing Characters ####

'''You can access individual characters in a string using indexing.
     Python uses zero-based indexing.
'''

my_string = "Hello"

print(my_string[0])  # Output: H

print(my_string[-1])  # Output: o


#### Slicing Strings  ####

my_string = "Hello, World!"

print(my_string[0:5])  # Output: Hello

print(my_string[7:])  # Output: World!

print(my_string[0:5:2])  # Output: Hlo


####  String Methods  ####

'''Changing Case
'''

my_string = "Hello, World!"

print(my_string.lower())  # Output: hello, world!
print(my_string.upper())  # Output: HELLO, WORLD!
print(my_string.capitalize())  # Output: Hello, world!
print(my_string.title())  # Output: Hello, World!

'''Searching and Replacing
'''

my_string = "Hello, World!"

print(my_string.find("World"))  # Output: 7
print(my_string.replace("World", "Python"))  # Output: Hello, Python!

'''Splitting and Joining
'''

my_string = "Hello, World!"

# Splitting a string into a list
split_str = my_string.split(", ")
print(split_str)  # Output: ['Hello', 'World!']

# Joining a list into a string
join_str = ", ".join(split_str)
print(join_str)  # Output: Hello, World!


'''Stripping Whitespace
'''

my_string = "   Hello, World!   "

print(my_string.strip())  # Output: Hello, World!
print(my_string.lstrip())  # Output: Hello, World!   
print(my_string.rstrip())  # Output:    Hello, World!


'''Checking Content
'''

my_string = "Hello123"

print(my_string.isalpha())  # Output: False
print(my_string.isdigit())  # Output: False
print(my_string.isalnum())  # Output: True
print(my_string.isspace())  # Output: False


####  Formatting Strings  ####

'''Using % Operator
'''

name = "Alice"
age = 30

print("Name: %s, Age: %d" % (name, age))  # Output: Name: Alice, Age: 30

'''Using str.format()
'''

name = "Alice"
age = 30

print("Name: {}, Age: {}".format(name, age))  # Output: Name: Alice, Age: 30
print("Name: {0}, Age: {1}".format(name, age))  # Output: Name: Alice, Age: 30
print("Name: {name}, Age: {age}".format(name=name, age=age))  # Output: Name: Alice, Age: 30


'''Using f-Strings (Python 3.6+)
'''

name = "Alice"
age = 30

print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 30


'''Escape Characters
'''

# Newline
print("Hello\nWorld!")  # Output: Hello
                        #         World!

# Tab
print("Hello\tWorld!")  # Output: Hello   World!

# Backslash
print("Hello\\World!")  # Output: Hello\World!

# Single quote
print('It\'s a string')  # Output: It's a string

# Double quote
print("He said, \"Hello\"")  # Output: He said, "Hello"


'''Multi-line Strings
'''

multi_line_str = """This is a
multi-line
string."""

print(multi_line_str)
# Output: This is a
#         multi-line
#         string.
