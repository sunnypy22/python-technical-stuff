# Basic File Operations

# Using open() with different modes

'''
'r': Read mode (default).
'w': Write mode. Creates a new file or truncates an existing file.
'a': Append mode. Creates a new file or appends to an existing file.
'b': Binary mode.
't': Text mode (default).
'+': Update mode. Allows reading and writing.
'''

# Reading Files

'''Reading the entire file
'''

with open('example.txt', 'r') as file:
    content = file.read()
print(content)

'''Reading line by line
'''

with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

'''Reading all lines into a list
'''

with open('example.txt', 'r') as file:
    lines = file.readlines()
print(lines)

# Writing Files

'''Writing to a file (overwriting)
'''

with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.")

'''Appending to a file
'''

with open('example.txt', 'a') as file:
    file.write("\nThis line is appended.")

# Working with Binary Files

'''Reading a binary file
'''

with open('example.bin', 'rb') as file:
    binary_content = file.read()
print(binary_content)

'''Writing to a binary file
'''

with open('example.bin', 'wb') as file:
    file.write(b'\x00\xFF\x00\xFF')


# Using Pathlib

'''The pathlib module offers an object-oriented approach to handle file operations.'''

'''Reading using Pathlib
'''

from pathlib import Path

file_path = Path('example.txt')
content = file_path.read_text()
print(content)

'''Writing using Pathlib
'''

from pathlib import Path

file_path = Path('example.txt')
file_path.write_text("Hello, World!\nThis is a new line.")


# Using io module

'''The io module provides tools for working with streams.'''

'''Reading using io.StringIO
'''

import io

text_stream = io.StringIO("Hello, World!\nThis is a new line.")
print(text_stream.read())

'''Writing using io.StringIO
'''

import io

text_stream = io.StringIO()
text_stream.write("Hello, World!\nThis is a new line.")
print(text_stream.getvalue())

# Using csv module

'''The csv module is useful for working with CSV files.'''

'''Reading a CSV file
'''

import csv

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

'''Writing to a CSV file
'''

import csv

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 30])
    writer.writerow(['Bob', 25])

# Using json module

'''The json module is useful for working with JSON files.'''

'''Reading a JSON file
'''

import json

with open('example.json', 'r') as file:
    data = json.load(file)
print(data)

'''Writing to a JSON file
'''

import json

data = {'name': 'Alice', 'age': 30}
with open('example.json', 'w') as file:
    json.dump(data, file)


# Using pickle module

'''The pickle module is useful for serializing and deserializing Python objects.'''

'''Reading a Pickle file
'''

import pickle

with open('example.pkl', 'rb') as file:
    data = pickle.load(file)
print(data)

'''Writing to a Pickle file
'''

import pickle

data = {'name': 'Alice', 'age': 30}
with open('example.pkl', 'wb') as file:
    pickle.dump(data, file)
