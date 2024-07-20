'''File handling in Python involves reading from and writing to files. 
    Python provides various built-in functions and methods to work with files.
      Here's an overview of different ways to handle files in Python:
'''

### Basic File Operations

#### 1. Opening Files

'''
You can open a file using the `open()` function, which returns a file object. 
The `open()` function takes two primary arguments: the file path and the mode.
'''

'''
**Modes**:
- `'r'`: Read (default mode).
- `'w'`: Write (creates a new file or truncates an existing file).
- `'a'`: Append (writes data to the end of the file).
- `'b'`: Binary mode (e.g., `'rb'` for reading binary files).
- `'t'`: Text mode (default).
'''

# **Example**:
file = open('example.txt', 'r')  # Open a file for reading

#### 2. Reading Files

# **Reading Entire File**:
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# **Reading Line by Line**:
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')

# **Reading a Specific Number of Characters**:
with open('example.txt', 'r') as file:
    content = file.read(10)  # Read the first 10 characters
    print(content)

# **Reading Lines into a List**:
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

#### 3. Writing to Files

# **Writing Data**:
with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a new line.')

# **Appending Data**:
with open('example.txt', 'a') as file:
    file.write('\nThis line is appended.')

#### 4. Working with Binary Files

# **Reading a Binary File**:
with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)

# **Writing to a Binary File**:
data = b'\x00\x01\x02'
with open('example.bin', 'wb') as file:
    file.write(data)

### Context Manager (`with` Statement)

'''
The `with` statement simplifies file handling by automatically closing the file when the
     block is exited, even if an exception is raised.
'''

# **Example**:
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed after the block

### File Operations with Path Objects (Python 3.4+)

# **Using `pathlib` for File Operations**:
from pathlib import Path

# Creating a Path object
path = Path('example.txt')

# Reading file content
content = path.read_text()
print(content)

# Writing to a file
path.write_text('Hello, World!')

# Appending to a file
with path.open('a') as file:
    file.write('\nAppended line.')

# Checking if a file exists
print(path.exists())

### Exception Handling

# **Handling Exceptions**:
try:
    with open('example.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('File not found.')
except IOError:
    print('Error reading file.')

### Summary
'''
- **Opening Files**: Use `open()` with appropriate modes.
- **Reading Files**: Methods include `read()`, `readline()`, `readlines()`, and 
    `for line in file`.
- **Writing to Files**: Use `write()` or `writelines()`.
- **Binary Files**: Open in binary mode (`'rb'`, `'wb'`).
- **Context Manager**: Use `with` to ensure files are properly closed.
- **Pathlib**: Use the `pathlib` module for an object-oriented approach to file operations.
'''