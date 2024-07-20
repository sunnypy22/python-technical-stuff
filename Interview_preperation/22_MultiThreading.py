'''Multithreading is a programming technique that allows multiple threads to
     be executed concurrently within a single process. This can be particularly useful
       for tasks that are I/O-bound or that require concurrent operations, like handling
         multiple user requests or performing background tasks.
'''
### Key Concepts in Multithreading

'''
1. **Thread**: The smallest unit of execution within a process. Threads within the same
     process share the same memory space and resources.

2. **Concurrency**: Multithreading enables concurrent execution of threads, which can make
     programs more efficient by allowing them to perform multiple tasks at the same time.

3. **GIL (Global Interpreter Lock)**: In CPython (the reference implementation of Python),
     the GIL is a mutex that protects access to Python objects, preventing multiple native 
     threads from executing Python bytecodes simultaneously. This means that Python
       threads are not truly parallel but are interleaved, which can limit
         performance benefits in CPU-bound tasks.

4. **Synchronization**: Techniques used to manage access to shared resources between threads 
    to avoid conflicts and ensure data integrity. Common synchronization mechanisms include 
    locks, semaphores, and condition variables.
'''

### Using Multithreading in Python
'''
Python provides the `threading` module to work with threads. Here are some examples of
 how to use it.
'''
#### 1. **Basic Multithreading Example**

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in 'abcde':
        time.sleep(1.5)
        print(letter)

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()
'''
In this example:
- Two functions (`print_numbers` and `print_letters`) run in parallel.
- `thread1` and `thread2` are created and started.
- `join()` is used to wait for both threads to finish before the program exits.
'''
#### 2. **Using Locks for Synchronization**

import threading

# Shared resource
counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100000):
        with lock:  # Acquire the lock
            counter += 1

# Create threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print(f"Final counter value: {counter}")
'''
In this example:
- A `lock` is used to synchronize access to the `counter` variable, preventing race conditions.
- The `with lock:` statement ensures that only one thread can modify the `counter` at a time.
'''
#### 3. **Thread Pool Using `concurrent.futures`**

from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    time.sleep(1)
    return f"Task {n} complete"

# Create a thread pool
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(5)]
    for future in futures:
        print(future.result())
'''
In this example:
- `ThreadPoolExecutor` is used to manage a pool of threads.
- `executor.submit()` schedules the `task` function to be executed in the pool.
- `future.result()` retrieves the result of the completed task.
'''
### Pros and Cons of Multithreading
'''
**Pros:**
1. **Responsiveness**: Multithreading can make applications more responsive by performing 
    background tasks concurrently.
2. **Concurrency**: Allows multiple tasks to be performed at the same time, improving overall
     efficiency.
3. **Resource Sharing**: Threads share the same memory space, which can simplify 
    communication between tasks.

**Cons:**
1. **Complexity**: Multithreading introduces complexity in terms of synchronization and debugging.
2. **GIL Limitation**: In CPython, the GIL can limit the performance of CPU-bound tasks, as 
    threads cannot fully utilize multiple CPU cores.
3. **Race Conditions**: Without proper synchronization, threads can lead to race conditions
     and inconsistent data.
'''
### When to Use Multithreading
'''
1. **I/O-Bound Tasks**: Tasks that involve waiting for external resources 
    (e.g., network or file I/O) can benefit from multithreading.
2. **Background Tasks**: Tasks that need to run concurrently in the background, 
    such as periodic updates or real-time data processing.
3. **Improving Responsiveness**: Applications that need to remain responsive
     while performing multiple operations.
'''