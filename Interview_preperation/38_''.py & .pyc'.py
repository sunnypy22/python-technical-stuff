'''In Python, `.py` and `.pyc` are file extensions associated with different types 
    of files used in the execution of Python code.
'''
### `.py` Files
'''
**Definition**: `.py` files are Python source files containing plain text code written
 in Python. These files include the Python code that you write and execute.
'''
'''
**Characteristics**:
- **Human-readable**: Contains the actual source code written in Python, which can be 
edited using a text editor or IDE.
- **Executable**: These files can be executed directly by the Python interpreter.
- **File Extension**: `.py`
'''

# **Example**:
# hello.py
print("Hello, World!")

'''
**Usage**:
- **Writing Code**: You write and edit your Python scripts or modules in `.py` files.
- **Execution**: You run `.py` files using the Python interpreter, e.g., `python hello.py`.
'''


### `.pyc` Files

'''
**Definition**: `.pyc` files are compiled Python files that contain the bytecode 
representation of the source code in `.py` files. Python compiles source code into
 bytecode, which is a lower-level, platform-independent representation of your source code.
'''

'''
**Characteristics**:
- **Not Human-readable**: Contains compiled bytecode, which is not meant to be read 
or edited by humans.
- **Generated Automatically**: Python automatically generates `.pyc` files when you 
run a `.py` file. These files are stored in the `__pycache__` directory.
- **File Extension**: `.pyc`
'''

# **Example**:
'''
- If you have a `hello.py` file, Python might generate a file named 
`hello.cpython-<version>.pyc` (e.g., `hello.cpython-38.pyc` for Python 3.8).
'''

'''
**Usage**:
- **Performance**: `.pyc` files are used to improve performance by skipping the 
compilation step when the Python script is run again.
- **Location**: Typically located in the `__pycache__` directory within the same 
directory as the `.py` file.
'''


### Key Differences
'''
1. **Content**:
   - `.py`: Contains source code written in Python.
   - `.pyc`: Contains compiled bytecode for faster execution.

2. **Readability**:
   - `.py`: Human-readable.
   - `.pyc`: Not human-readable (binary format).

3. **Generation**:
   - `.py`: Created by the user.
   - `.pyc`: Automatically generated by Python when a `.py` file is executed.

4. **Purpose**:
   - `.py`: Used for writing and editing Python code.
   - `.pyc`: Used for performance optimization by storing compiled bytecode.
'''

### Managing `.pyc` Files
'''
- **Cleaning Up**: `.pyc` files can be safely deleted if you need to clear space or resolve issues. They will be regenerated the next time the corresponding `.py` file is executed.
- **Disabling Compilation**: You can disable the generation of `.pyc` files by setting the environment variable `PYTHONPYCACHEPREFIX` to an empty string or by using the `-B` command line option: `python -B script.py`.
'''

### Summary
'''
- **`.py` Files**: Python source code files that are written and edited by developers.
- **`.pyc` Files**: Compiled bytecode files generated by Python to optimize performance during execution.
'''