'''
Asynchronous programming allows tasks to be executed independently of the main
 program flow, enabling a program to perform other operations while waiting
   for certain tasks (such as I/O operations) to complete. This can improve efficiency
     and responsiveness, especially in applications that involve long-running operations or
       multiple I/O tasks.
'''

### Key Concepts in Asynchronous Programming
'''
1. **Concurrency**: Running multiple tasks simultaneously. Asynchronous programming is
     one way to achieve concurrency, but not the only one. Other methods include
       multithreading and multiprocessing.

2. **Event Loop**: A core concept in asynchronous programming that continuously checks
     for tasks that are ready to be executed and manages the scheduling of these tasks.

3. **Future/Promise**: A construct that represents a result that
     will be available in the future. In Python, this is represented by `Future`
       objects in libraries like `asyncio`.

4. **Callback**: A function passed as an argument to another function,
     which is invoked after the completion of the initial function.

5. **Coroutines**: Special functions in Python defined with `async def`, which can
     be paused and resumed with the `await` keyword. They are used to perform asynchronous 
     operations.
'''
### Asynchronous Programming in Python

'''
Python provides several ways to implement asynchronous programming, most
 notably through the `asyncio` library. Here's an overview and examples of how to use it.
'''
#### 1. **Basic Asynchronous Function Example**
'''
Using `asyncio` to define and run asynchronous functions:
'''
import asyncio

async def async_task1():
    print("Task 1 is starting")
    await asyncio.sleep(2)  # Simulate a long-running task
    print("Task 1 is complete")

async def async_task2():
    print("Task 2 is starting")
    await asyncio.sleep(1)  # Simulate a long-running task
    print("Task 2 is complete")

async def main():
    await asyncio.gather(
        async_task1(),
        async_task2()
    )

# Run the main function
asyncio.run(main())
'''
In this example:
- `async_task1` and `async_task2` are asynchronous functions that use `await` to pause execution while waiting.
- `asyncio.gather` is used to run both tasks concurrently.
'''
#### 2. **Asynchronous HTTP Requests**
'''
Using `aiohttp` to make asynchronous HTTP requests:
'''
import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url1 = 'https://api.example.com/data1'
    url2 = 'https://api.example.com/data2'
    
    # Fetch data concurrently
    data1, data2 = await asyncio.gather(fetch(url1), fetch(url2))
    print(f"Data from {url1}: {data1[:100]}")  # Print first 100 characters
    print(f"Data from {url2}: {data2[:100]}")  # Print first 100 characters

# Run the main function
asyncio.run(main())
'''
In this example:
- `fetch` is an asynchronous function that makes an HTTP request and retrieves the response.
- `asyncio.gather` is used to run multiple `fetch` operations concurrently.
'''
#### 3. **Asynchronous File I/O**
'''
Using `aiofiles` for asynchronous file operations:
'''
import aiofiles
import asyncio

async def read_file(file_path):
    async with aiofiles.open(file_path, mode='r') as file:
        content = await file.read()
    return content

async def write_file(file_path, content):
    async with aiofiles.open(file_path, mode='w') as file:
        await file.write(content)

async def main():
    content = await read_file('input.txt')
    print(f"Read content: {content[:100]}")  # Print first 100 characters
    await write_file('output.txt', content)

# Run the main function
asyncio.run(main())

'''
In this example:
- `read_file` and `write_file` are asynchronous functions for reading from and writing to files.
'''

### Pros and Cons of Asynchronous Programming
'''
**Pros:**
1. **Improved Efficiency**: Asynchronous operations allow other tasks to be executed while waiting for I/O operations to complete, improving overall efficiency.
2. **Better Responsiveness**: Ideal for applications that need to remain responsive while performing background tasks, such as web servers or GUI applications.
3. **Concurrency**: Allows for concurrent execution of tasks without requiring multiple threads or processes.

**Cons:**
1. **Complexity**: Asynchronous programming can introduce complexity into code, making it harder to understand and debug.
2. **Error Handling**: Managing errors and exceptions in asynchronous code can be more challenging compared to synchronous code.
'''
### When to Use Asynchronous Programming
'''
1. **I/O-Bound Applications**: Applications that perform a lot of I/O operations, such as web servers, network clients, or applications with file operations.
2. **Real-Time Systems**: Systems that require real-time responsiveness and need to handle multiple tasks concurrently.
3. **Scalable Systems**: Applications that need to handle a large number of simultaneous connections or requests efficiently.
'''
