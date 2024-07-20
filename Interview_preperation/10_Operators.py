'''Operators in Python are special symbols or keywords that are used to 
perform operations on variables and values. 
Python supports a variety of operators, each serving a different purpose.
'''

'''
1. **Arithmetic Operators**
2. **Comparison (Relational) Operators**
3. **Assignment Operators**
4. **Logical Operators**
5. **Bitwise Operators**
6. **Membership Operators**
7. **Identity Operators**
'''

### 1. Arithmetic Operators

'''
These operators are used to perform mathematical operations like addition, 
subtraction, multiplication, etc.

| Operator | Description       | Example          |
|----------|-------------------|------------------|
| `+`      | Addition          | `a + b`          |
| `-`      | Subtraction       | `a - b`          |
| `*`      | Multiplication    | `a * b`          |
| `/`      | Division          | `a / b`          |
| `%`      | Modulus           | `a % b`          |
| `**`     | Exponentiation    | `a ** b`         |
| `//`     | Floor Division    | `a // b`         |
'''

#### Example:

a = 10
b = 3

print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333333333333335
print(a % b)  # Output: 1
print(a ** b) # Output: 1000
print(a // b) # Output: 3

### 2. Comparison (Relational) Operators

'''
These operators compare the values of two operands and return `True` or `False` 
based on the condition.

| Operator | Description              | Example     |
|----------|--------------------------|-------------|
| `==`     | Equal to                 | `a == b`    |
| `!=`     | Not equal to             | `a != b`    |
| `>`      | Greater than             | `a > b`     |
| `<`      | Less than                | `a < b`     |
| `>=`     | Greater than or equal to | `a >= b`    |
| `<=`     | Less than or equal to    | `a <= b`    |
'''

#### Example:

a = 10
b = 3

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: True
print(a < b)   # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False

### 3. Assignment Operators

'''
These operators are used to assign values to variables.

| Operator | Description              | Example     |
|----------|--------------------------|-------------|
| `=`      | Assign                   | `a = 5`     |
| `+=`     | Add and assign           | `a += 3`    |
| `-=`     | Subtract and assign      | `a -= 3`    |
| `*=`     | Multiply and assign      | `a *= 3`    |
| `/=`     | Divide and assign        | `a /= 3`    |
| `%=`     | Modulus and assign       | `a %= 3`    |
| `//=`    | Floor divide and assign  | `a //= 3`   |
| `**=`    | Exponentiate and assign  | `a **= 3`   |
| `&=`     | Bitwise AND and assign   | `a &= 3`    |
| `|=`     | Bitwise OR and assign    | `a |= 3`    |
| `^=`     | Bitwise XOR and assign   | `a ^= 3`    |
| `>>=`    | Bitwise right shift and assign | `a >>= 3` |
| `<<=`    | Bitwise left shift and assign  | `a <<= 3` |
'''
#### Example:

a = 10

a += 3
print(a)  # Output: 13

a -= 3
print(a)  # Output: 10

a *= 3
print(a)  # Output: 30

a /= 3
print(a)  # Output: 10.0

### 4. Logical Operators
'''
These operators are used to perform logical operations on boolean values.

| Operator | Description              | Example         |
|----------|--------------------------|-----------------|
| `and`    | Logical AND              | `a and b`       |
| `or`     | Logical OR               | `a or b`        |
| `not`    | Logical NOT              | `not a`         |
'''

#### Example:

a = True
b = False

print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False

### 5. Bitwise Operators
'''
These operators are used to perform bit-level operations on binary numbers.

| Operator | Description            | Example         |
|----------|------------------------|-----------------|
| `&`      | Bitwise AND            | `a & b`         |
| `|`      | Bitwise OR             | `a | b`         |
| `^`      | Bitwise XOR            | `a ^ b`         |
| `~`      | Bitwise NOT            | `~a`            |
| `<<`     | Bitwise left shift     | `a << b`        |
| `>>`     | Bitwise right shift    | `a >> b`        |
'''
#### Example:

a = 10  # 1010 in binary
b = 4   # 0100 in binary

print(a & b)  # Output: 0
print(a | b)  # Output: 14
print(a ^ b)  # Output: 14
print(~a)     # Output: -11
print(a << 2) # Output: 40
print(a >> 2) # Output: 2

### 6. Membership Operators
'''
These operators are used to test if a value is found within a 
sequence (such as a string, list, or tuple).

| Operator | Description              | Example         |
|----------|--------------------------|-----------------|
| `in`     | Evaluates to True if it finds a variable in the specified sequence | `a in b`  |
| `not in` | Evaluates to True if it does not find a variable in the 
             specified sequence | `a not in b` |
'''
#### Example:

a = 10
b = [10, 20, 30, 40]

print(a in b)      # Output: True
print(a not in b)  # Output: False

### 7. Identity Operators
'''
These operators are used to compare the memory locations of two objects.

| Operator | Description              | Example         |
|----------|--------------------------|-----------------|
| `is`     | Evaluates to True if the variables on either side of the operator point to the same object | `a is b`  |
| `is not` | Evaluates to True if the variables on either side of the operator do not point to the same object | `a is not b` |
'''
#### Example:

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)      # Output: False
print(a is c)      # Output: True
print(a is not b)  # Output: True

