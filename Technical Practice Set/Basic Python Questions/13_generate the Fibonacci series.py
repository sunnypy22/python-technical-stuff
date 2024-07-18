# 1. Iterative Approach

def fibonacci_series_iterative(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

n = 10
print(f"Fibonacci series up to {n} terms: {fibonacci_series_iterative(n)}")

# 2. Recursive Approach

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci_recursive(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

n = 10
print(f"Fibonacci series up to {n} terms: {fibonacci_recursive(n)}")

# 3. Dynamic Programming with Memoization (Top-Down)

def fibonacci_memoization(n, memo={0: 0, 1: 1}):
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

def generate_fibonacci_series_memoization(n):
    return [fibonacci_memoization(i) for i in range(n)]

n = 10
print(f"Fibonacci series up to {n} terms: {generate_fibonacci_series_memoization(n)}")


# 4. Using List Comprehension

def fibonacci_list_comprehension(n):
    fib_series = [0, 1]
    [fib_series.append(fib_series[-1] + fib_series[-2]) for _ in range(2, n)]
    return fib_series[:n]

n = 10
print(f"Fibonacci series up to {n} terms: {fibonacci_list_comprehension(n)}")

# 5. Using a Generator

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def generate_fibonacci_series_generator(n):
    fib_gen = fibonacci_generator()
    return [next(fib_gen) for _ in range(n)]

n = 10
print(f"Fibonacci series up to {n} terms: {generate_fibonacci_series_generator(n)}")
