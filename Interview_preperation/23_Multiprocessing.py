'''Multiprocessing is a programming technique that allows multiple processes to run 
    concurrently. Unlike multithreading, where threads share the same memory space
         and are limited by the Global Interpreter Lock (GIL) in CPython, 
         multiprocessing involves creating separate processes that have their own memory
           space. This allows true parallel execution, which can be beneficial for 
           CPU-bound tasks.
'''
### Key Concepts in Multiprocessing

'''
1. **Process**: An independent unit of execution with its own memory space.
     Processes do not share memory with other processes, which can help
       avoid issues related to shared state.

2. **Concurrency**: Like multithreading, multiprocessing enables concurrent 
    execution of tasks, but it does so using separate processes.

3. **Inter-Process Communication (IPC)**: Mechanisms for processes to communicate and
     synchronize with each other, such as queues, pipes, and shared memory.

4. **True Parallelism**: Unlike threads, processes can run in parallel on 
    multiple CPU cores, making multiprocessing suitable for CPU-bound tasks.
'''
### Using Multiprocessing in Python
'''
Python provides the `multiprocessing` module to work with processes. Here are some examples:
'''
#### 1. **Basic Multiprocessing Example**

from multiprocessing import Process
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Number: {i}")

def print_letters():
    for letter in 'abcde':
        time.sleep(1.5)
        print(f"Letter: {letter}")

if __name__ == "__main__":
    # Create processes
    process1 = Process(target=print_numbers)
    process2 = Process(target=print_letters)

    # Start processes
    process1.start()
    process2.start()

    # Wait for processes to complete
    process1.join()
    process2.join()
'''
In this example:
- Two functions (`print_numbers` and `print_letters`) are executed in parallel using
     separate processes.
- `start()` is used to begin the execution of each process.
- `join()` ensures that the main program waits for both processes to complete before exiting.
'''
#### 2. **Using Queues for Inter-Process Communication**

from multiprocessing import Process, Queue

def worker(queue):
    queue.put("Hello from process")

def main():
    queue = Queue()
    process = Process(target=worker, args=(queue,))
    process.start()
    process.join()
    message = queue.get()
    print(f"Received message: {message}")

if __name__ == "__main__":
    main()
'''
In this example:
- A `Queue` is used for communication between processes.
- The `worker` function puts a message in the queue, and the main function retrieves it
     after the process completes.
'''
#### 3. **Using Shared Memory**

from multiprocessing import Process, Value, Array

def modify_data(shared_value, shared_array):
    shared_value.value += 1
    for i in range(len(shared_array)):
        shared_array[i] += 1

def main():
    shared_value = Value('i', 0)  # Shared integer
    shared_array = Array('i', range(5))  # Shared array

    process = Process(target=modify_data, args=(shared_value, shared_array))
    process.start()
    process.join()

    print(f"Shared value: {shared_value.value}")
    print(f"Shared array: {list(shared_array)}")

if __name__ == "__main__":
    main()
'''
In this example:
- `Value` and `Array` are used to create shared memory objects that can be modified by
     different processes.
'''
### Pros and Cons of Multiprocessing
'''
**Pros:**
1. **True Parallelism**: Processes can run on multiple CPU cores, which is beneficial for
     CPU-bound tasks.
2. **Isolation**: Each process has its own memory space, reducing issues related to shared
     state and making debugging easier.
3. **No GIL Limitation**: Unlike threads, processes are not affected by the Global
     Interpreter Lock (GIL), allowing for true parallel execution.

**Cons:**
1. **Higher Overhead**: Creating and managing processes can be more resource-intensive compared
     to threads.
2. **Complexity**: Inter-process communication and synchronization can be more complex than
     managing threads.
3. **Resource Consumption**: Multiple processes can consume more memory and other resources 
    compared to threads.
'''
### When to Use Multiprocessing
'''
1. **CPU-Bound Tasks**: Tasks that require heavy computation and can benefit from true
     parallelism.
2. **Heavy Parallel Processing**: Scenarios where tasks can be divided into independent
     units of work that can be processed simultaneously.
3. **Isolation Needed**: Applications where processes need to run in isolation to prevent
     interference and maintain data integrity.
'''