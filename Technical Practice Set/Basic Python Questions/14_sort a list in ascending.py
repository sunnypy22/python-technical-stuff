# 1. Using the sort() Method

def sort_list_in_place(lst):
    lst.sort()

# Example usage
numbers = [5, 2, 9, 1, 5, 6]
sort_list_in_place(numbers)
print(f"Sorted list: {numbers}")

# 2. Using the sorted() Function

def sort_list_new(lst):
    return sorted(lst)

# Example usage
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sort_list_new(numbers)
print(f"Original list: {numbers}")
print(f"Sorted list: {sorted_numbers}")

# 3. Implementing Bubble Sort

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

# Example usage
numbers = [5, 2, 9, 1, 5, 6]
bubble_sort(numbers)
print(f"Sorted list: {numbers}")

# 4. Implementing QuickSort

def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Example usage
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = quicksort(numbers)
print(f"Sorted list: {sorted_numbers}")
