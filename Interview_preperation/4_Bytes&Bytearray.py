'''In Python, `bytes` and `bytearray` are data types used to handle binary data. 
They are similar in many ways but have key differences, particularly in mutability.
'''
### `bytes`

'''
- Immutable: Once created, the contents of a `bytes` object cannot be modified.
- Usage: Often used for binary data, such as files or network packets.
- Syntax: Created using the `bytes` constructor, a byte literal, or by encoding a string.
'''


#### Examples:

# Creating bytes from a string
b = bytes('hello', 'utf-8')
print(b)  # Output: b'hello'

# Creating bytes from a list of integers
b = bytes([104, 101, 108, 108, 111])
print(b)  # Output: b'hello'

# Byte literal
b = b'hello'
print(b)  # Output: b'hello'

### `bytearray`

'''
- Mutable The contents of a `bytearray` object can be modified after creation.
- Usage: Useful when you need a mutable sequence of bytes.
- Syntax Created using the `bytearray` constructor, which can take the same
 arguments as the `bytes` constructor.
'''

#### Examples:

# Creating bytearray from a string
ba = bytearray('hello', 'utf-8')
print(ba)  # Output: bytearray(b'hello')

# Creating bytearray from a list of integers
ba = bytearray([104, 101, 108, 108, 111])
print(ba)  # Output: bytearray(b'hello')

# Modifying a bytearray
ba[0] = 72  # Changing 'h' to 'H'
print(ba)  # Output: bytearray(b'Hello')

### Key Differences

'''
1. **Mutability**:
   - `bytes` is immutable.
   - `bytearray` is mutable.

2. **Use Cases**:
   - `bytes` is suitable for data that should not change, like keys in cryptographic
         operations or raw bytes from network sources.
   - `bytearray` is suitable when you need to modify binary data,
         such as constructing a binary protocol.

3. **Initialization**:
   - Both `bytes` and `bytearray` can be initialized with a string and 
        an encoding, a list of integers, or another bytes-like object.

4. **Memory Efficiency**:
   - `bytes` objects are slightly more memory efficient due to immutability.

'''   


### Operations

#### Common Operations


'''
Both `bytes` and `bytearray` support common sequence operations:
'''
# Length
print(len(b))  # Output: 5

# Indexing
print(b[0])  # Output: 104 (ASCII value of 'h')

# Slicing
print(b[1:4])  # Output: b'ell'

#### `bytearray` Specific Operations

'''Since `bytearray` is mutable, you can modify its contents:
'''

# Changing elements
ba[1:4] = b'EL'  # Modifying slice
print(ba)  # Output: bytearray(b'HELL')

# Appending elements
ba.append(33)  # Appending '!'
print(ba)  # Output: bytearray(b'HELLO!')

# Extending with another sequence
ba.extend(b' world')
print(ba)  # Output: bytearray(b'HELLO! world')

### Conversions

'''You can convert between `bytes` and `bytearray`:
'''

# bytes to bytearray
b = b'hello'
ba = bytearray(b)
print(ba)  # Output: bytearray(b'hello')

# bytearray to bytes
ba = bytearray(b'hello')
b = bytes(ba)
print(b)  # Output: b'hello'

### Summary

'''
- **`bytes`**: Immutable sequence of bytes, useful for fixed binary data.
- **`bytearray`**: Mutable sequence of bytes, useful for when you need to modify the binary data.
'''
