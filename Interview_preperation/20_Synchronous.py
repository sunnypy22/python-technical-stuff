'''
Synchronous operations in programming are those where tasks are executed one after another.
 Each task must complete before the next one begins.
   This sequential execution can lead to waiting periods if one
     task takes a long time to complete, as subsequent tasks cannot proceed until the
       current task finishes.
'''

### Synchronous Programming in Python

'''
In Python, most standard code execution is synchronous. Let's look at some examples:
'''

### Example 1: Basic Synchronous Execution

def task1():
    print("Task 1 is starting")
    # Simulating a long-running task
    for _ in range(5):
        print("Task 1 is running")
    print("Task 1 is complete")

def task2():
    print("Task 2 is starting")
    # Simulating a long-running task
    for _ in range(5):
        print("Task 2 is running")
    print("Task 2 is complete")

task1()
task2()

### Example 2: Synchronous File Reading and Writing
'''
Reading from a file and then writing to another file synchronously:
'''
def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)

# Reading data from a file
data = read_file('input.txt')
# Writing data to another file
write_file('output.txt', data)

### Example 3: Synchronous HTTP Requests
'''
Using the `requests` library to make synchronous HTTP requests:
'''
import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

url1 = 'https://api.example.com/data1'
url2 = 'https://api.example.com/data2'

data1 = fetch_data(url1)
print(f"Data from {url1}: {data1}")

data2 = fetch_data(url2)
print(f"Data from {url2}: {data2}")

### Pros and Cons of Synchronous Programming
'''
**Pros:**
1. **Simplicity**: Synchronous code is straightforward and easier to understand and debug.
2. **Deterministic Execution**: The sequence of operations is predictable, 
making it easier to trace the flow of execution.

**Cons:**
1. **Blocking**: If a task takes a long time to complete, 
    it blocks the execution of subsequent tasks, leading to inefficiencies.
2. **Inefficiency**: In applications that involve I/O operations 
    (like network requests or file operations), synchronous execution can be inefficient
    as it waits for each operation to complete.

### When to Use Synchronous Programming

1. **Simple Scripts**: For straightforward tasks that don't involve heavy I/O 
    operations or require concurrency.
2. **Deterministic Execution**: When the order of execution is crucial and you
     need tasks to complete in a specific sequence.
3. **Simplicity**: When ease of understanding and simplicity are more important 
    than performance optimization.
'''
