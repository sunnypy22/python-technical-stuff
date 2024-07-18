
# 1. Using the sort() Method with reverse=True

def sort_list_in_place_descending(lst):
    lst.sort(reverse=True)

# Example usage
numbers = [5, 2, 9, 1, 5, 6]
sort_list_in_place_descending(numbers)
print(f"Sorted list (descending): {numbers}")

# 2. Using the sorted() Function with reverse=True

def sort_list_new_descending(lst):
    return sorted(lst, reverse=True)

# Example usage
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sort_list_new_descending(numbers)
print(f"Original list: {numbers}")
print(f"Sorted list (descending): {sorted_numbers}")

# 3. Implementing Bubble Sort (Descending Order)

def bubble_sort_descending(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

# Example usage
numbers = [5, 2, 9, 1, 5, 6]
bubble_sort_descending(numbers)
print(f"Sorted list (descending): {numbers}")

# 4. Implementing QuickSort (Descending Order)

def quicksort_descending(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x > pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x < pivot]
    return quicksort_descending(left) + middle + quicksort_descending(right)

# Example usage
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = quicksort_descending(numbers)
print(f"Sorted list (descending): {sorted_numbers}")
