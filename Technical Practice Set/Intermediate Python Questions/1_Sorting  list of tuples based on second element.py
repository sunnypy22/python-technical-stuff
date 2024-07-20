# 1. Using sorted() with a lambda function

data = [(1, 3), (4, 1), (5, 2), (2, 4)]

sorted_data = sorted(data, key=lambda x: x[1])
print("Sorted using lambda:", sorted_data)

# 2. Using a custom function


data = [(1, 3), (4, 1), (5, 2), (2, 4)]

def get_second_element(tuple):
    return tuple[1]

sorted_data = sorted(data, key=get_second_element)
print("Sorted using custom function:", sorted_data)

data.sort(key=get_second_element)
print("Sorted using sort() and custom function:", data)
