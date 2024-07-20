'''Control flow in Python refers to the order in which individual statements, 
instructions, or function calls are executed or evaluated in a program. 
Python supports several control flow constructs that allow you to manage the execution
 flow of your program. 
 These constructs include conditional statements, loops, and control flow altering statements.
'''
### 1. Conditional Statements
'''
Conditional statements allow you to execute certain pieces of code based on whether a
 condition is true or false. The primary conditional statements in
   Python are `if`, `elif`, and `else`.
'''
#### Example:

x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

### 2. Loops
'''
Loops are used to execute a block of code repeatedly. Python supports two main types
 of loops: `for` and `while`.
'''
#### a. `for` Loop
'''
The `for` loop iterates over a sequence (such as a list, tuple, dictionary, set, or string)
 and executes a block of code for each item in the sequence.
'''
##### Example:

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a range
for i in range(5):
    print(i)

#### b. `while` Loop

'''
The `while` loop repeatedly executes a block of code as long as a specified condition
 is true.
'''
##### Example:

count = 0
while count < 5:
    print(count)
    count += 1

### 3. Control Flow Altering Statements
'''
These statements alter the normal flow of control in a program. 
Python includes `break`, `continue`, and `pass`.
'''
#### a. `break`
'''
The `break` statement terminates the nearest enclosing loop.
'''
##### Example:

for i in range(10):
    if i == 5:
        break
    print(i)

#### b. `continue`
'''
The `continue` statement skips the rest of the code inside the loop for
 the current iteration and moves to the next iteration.
'''
##### Example:

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#### c. `pass`
'''
The `pass` statement is a null operation; it does nothing. It can be used as
 a placeholder for future code.
'''
##### Example:

for i in range(10):
    if i % 2 == 0:
        pass  # Placeholder for future code
    else:
        print(i)

### 4. Exception Handling
'''
Python provides a way to handle exceptions (errors) using `try`, `except`, `else`,
 and `finally` blocks.
'''
#### Example:

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("No exceptions occurred")
finally:
    print("This block is always executed")

### 5. `match` Statement (Python 3.10+)
'''
The `match` statement allows for pattern matching, which can be seen
 as a more powerful form of the `switch` statement found in other languages.
'''
#### Example:
'''
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

print(http_status(200))  # Output: OK

'''