'''Memory management in Python is crucial for efficient resource utilization and 
    to prevent memory leaks and other issues. Python uses several techniques and
      mechanisms to manage memory, including garbage collection, reference counting,
        and memory allocation strategies. Here’s a detailed overview:
'''

### 1. **Reference Counting**
'''
- **Concept**: Each object in Python has an associated reference count,
     which tracks the number of references to the object. When an object's reference
       count drops to zero, it means no one is using it, and the memory occupied by
         the object can be reclaimed.
- **Mechanism**: Python automatically manages the reference counts of objects. When 
        a reference is made to an object, its count increases, and when a reference is deleted,
        the count decreases. If the count reaches zero, Python frees the memory.
'''

# **Example:**

import sys

a = []  # Reference count of list starts at 1
b = a   # Reference count of list increases to 2
print(sys.getrefcount(a))  # Output: 3 (including the count in getrefcount)

### 2. **Garbage Collection**
'''
- **Concept**: Python's garbage collector deals with cyclic references that reference 
    counting alone cannot handle. It identifies and cleans up groups of objects that
         reference each other but are no longer reachable from the program.
- **Mechanism**: Python uses a cyclic garbage collector to detect cycles of references 
    and clean them up. This is part of the `gc` module.
'''

# **Example:**

import gc

# Enable garbage collection
gc.enable()

# Manually trigger garbage collection
gc.collect()
'''
**Key Points:**
- **Generational Approach**: Python’s garbage collector uses a generational approach,
     with three generations. Objects are initially allocated in the first generation and
       promoted to higher generations if they survive multiple garbage collection cycles.
- **Thresholds**: Collection occurs based on thresholds set for each generation.
'''
### 3. **Memory Allocation**
'''
- **Concept**: Python uses memory pools and allocators to manage memory efficiently.
     The default allocator is designed to handle small objects efficiently.
- **Mechanism**: Python’s memory manager uses a system called `pymalloc` to allocate memory
     in blocks for small objects. It also relies on the OS’s memory allocator for
       larger objects.

**Key Points:**
- **Object-Specific Allocators**: Python has specialized allocators for different types
     of objects, such as integers, lists, and dictionaries.
- **Memory Pools**: Memory for small objects is allocated in pools to reduce
     fragmentation and improve performance.
'''
### 4. **Memory Management for Built-in Types**
'''
- **Immutable Types**: Strings, integers, and tuples are immutable. Python optimizes
     memory usage for these types by reusing objects where possible.
- **Mutable Types**: Lists, sets, and dictionaries are mutable. Python’s memory management
     ensures that changes to these types are efficiently handled.
'''

# **Example:**

# Immutable objects
x = 10
y = 10
print(x is y)  # Output: True (Python reuses small integers)

# Mutable objects
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # Output: False (Different objects)

### 5. **Custom Memory Management**
'''
- **Concept**: For advanced usage, you might need to manage memory explicitly, such
     as when dealing with large datasets or performance-critical applications.
- **Mechanism**: You can use the `gc` module to fine-tune garbage collection or use
     libraries such as `numpy` for efficient array operations.
'''
# **Example:**

import gc

# Disable garbage collection for performance reasons
gc.disable()

# Perform memory-intensive operations

# Re-enable garbage collection
gc.enable()

### Summary
'''
- **Reference Counting**: Manages memory by counting references to objects and deallocating 
    memory when counts drop to zero.
- **Garbage Collection**: Detects and cleans up cyclic references that reference counting 
    cannot handle, using a generational approach.
- **Memory Allocation**: Utilizes memory pools and allocators to manage small and large
     objects efficiently.
- **Built-in Types**: Python optimizes memory for immutable types and handles mutable types 
    with specialized allocators.
- **Custom Management**: Advanced usage may involve manual tuning of garbage collection or
     using specialized libraries.
'''