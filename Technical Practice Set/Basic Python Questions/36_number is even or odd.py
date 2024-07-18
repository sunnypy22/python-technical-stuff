# 1. Using Modulo Operator (%)

'''The modulo operator helps determine the remainder of a division operation. For even numbers, 
number % 2 will be 0, and for odd numbers, it will be 1.'''

def even_or_odd_modulo(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
num = 7
print(f"{num} is {even_or_odd_modulo(num)}")

# 2. Using Bitwise AND Operator (&)

def even_or_odd_bitwise(number):
    if number & 1:
        return "Odd"
    else:
        return "Even"

# Example usage
num = 12
print(f"{num} is {even_or_odd_bitwise(num)}")

# 3. Using Integer Division (//)

def even_or_odd_integer_division(number):
    if number // 2 * 2 == number:
        return "Even"
    else:
        return "Odd"

# Example usage
num = 5
print(f"{num} is {even_or_odd_integer_division(num)}")

