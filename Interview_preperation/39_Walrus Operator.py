'''
The walrus operator (`:=`), introduced in Python 3.8, is used for assignment expressions. 
It allows you to assign a value to a variable as part of an expression. 
This can make your code more concise and sometimes more readable by combining assignment 
and expression evaluation in a single statement.
'''
### Syntax and Usage

'''
**Syntax**:
variable := expression
'''

'''
**Usage**:
- **Inline Assignment**: The walrus operator is often used when you want to assign
     a value to a variable and use it immediately in an expression.
- **Loop Conditions**: It can simplify code in loops and conditional statements.
'''


### Examples

#### Example 1: Inline Assignment in Expressions

# **Without Walrus Operator**:
# Read a line of input
line = input("Enter a line: ")
if line:
    print(f"Line: {line}")

# **With Walrus Operator**:
# Using the walrus operator for inline assignment
if (line := input("Enter a line: ")):
    print(f"Line: {line}")

'''
In this example, the walrus operator assigns the result of `input()` to `line` 
    and then checks if `line` is truthy in one step.
'''

#### Example 2: Simplifying Loops

# **Without Walrus Operator**:
lines = []
while True:
    line = input("Enter a line (or 'exit' to quit): ")
    if line == 'exit':
        break
    lines.append(line)
print("Lines entered:", lines)

# **With Walrus Operator**:
lines = []
while (line := input("Enter a line (or 'exit' to quit): ")) != 'exit':
    lines.append(line)
print("Lines entered:", lines)

'''
Here, the walrus operator helps to simplify the loop by combining the input assignment 
and condition check into one line.
'''

#### Example 3: List Comprehensions and Generator Expressions

# **Without Walrus Operator**:
# Example with list comprehension
'''results = [process(x) for x in data if process(x) > threshold]'''


# **With Walrus Operator**:
# Using walrus operator to avoid duplicate function calls
'''results = [result for x in data if (result := process(x)) > threshold]'''


'''
In this example, the walrus operator avoids calling `process(x)` twice by storing its 
    result in `result` and using it in both the condition and the result list.
'''
### Pros and Cons

'''
**Pros**:
- **Conciseness**: Reduces the need for additional lines of code.
- **Clarity**: Can make code more readable by reducing redundancy.
- **Performance**: Can improve performance by avoiding redundant calculations.

**Cons**:
- **Readability**: May reduce readability if overused or used in complex expressions.
- **Compatibility**: Not available in Python versions prior to 3.8, which may impact 
    code portability.
'''
