# 1. Naive Approach with Trial Division

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes_up_to(limit):
    return [num for num in range(2, limit + 1) if is_prime(num)]

# Example usage
limit = 30
prime_numbers = generate_primes_up_to(limit)
print(f"Prime numbers up to {limit}: {prime_numbers}")

# 2. Sieve of Eratosthenes

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not primes
    p = 2
    while (p * p <= limit):
        if primes[p] == True:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(limit + 1) if primes[p]]

# Example usage
limit = 30
prime_numbers = sieve_of_eratosthenes(limit)
print(f"Prime numbers up to {limit}: {prime_numbers}")

