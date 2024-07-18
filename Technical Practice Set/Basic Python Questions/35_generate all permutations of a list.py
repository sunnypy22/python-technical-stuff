# 1. Using itertools.permutations

'''The itertools module in Python provides a permutations function that generates
 all possible permutations of a sequence (or iterable). Here’s how you can use it:'''


from itertools import permutations

def generate_permutations(lst):
    return list(permutations(lst))

# Example usage
my_list = [1, 2, 3]
all_permutations = generate_permutations(my_list)

# Print all permutations
for perm in all_permutations:
    print(perm)

# 2. Using Recursion with Backtracking

'''You can implement a recursive function to generate permutations manually. 
This approach typically involves swapping elements to explore different permutations
 recursively.'''

def generate_permutations_recursive(lst, start=0):
    if start == len(lst):
        print(lst)
    else:
        for i in range(start, len(lst)):
            # Swap elements
            lst[start], lst[i] = lst[i], lst[start]
            # Recursively generate permutations for the rest of the list
            generate_permutations_recursive(lst, start + 1)
            # Backtrack: swap back the elements
            lst[start], lst[i] = lst[i], lst[start]

# Example usage
my_list = [1, 2, 3]
generate_permutations_recursive(my_list)
