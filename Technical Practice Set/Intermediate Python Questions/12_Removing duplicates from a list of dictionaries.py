# Method 1: Using a Set for Unique Keys

'''Convert dictionaries to a set of tuples (where each tuple represents a dictionary)
 to automatically handle duplicates.'''

def remove_duplicates_dicts(lst):
    return list({frozenset(d.items()): d for d in lst}.values())

# Example usage
dict_list = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Alice', 'age': 30}
]

print(remove_duplicates_dicts(dict_list))  # Output: [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

# Method 2: Using a Set with a Custom Key Function

'''Use a set to keep track of seen items and filter out duplicates based on a custom key.'''

def remove_duplicates_dicts_custom_key(lst):
    seen = set()
    result = []
    for d in lst:
        # Convert dictionary to a frozenset of its items for immutability
        key = frozenset(d.items())
        if key not in seen:
            seen.add(key)
            result.append(d)
    return result

# Example usage
dict_list = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Alice', 'age': 30}
]

print(remove_duplicates_dicts_custom_key(dict_list))  # Output: [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

# Method 3: Using List Comprehension with a Set

'''Use a list comprehension with a set to keep track of seen dictionaries.'''

def remove_duplicates_dicts_list_comprehension(lst):
    seen = set()
    return [d for d in lst if not (frozenset(d.items()) in seen or seen.add(frozenset(d.items())))]

# Example usage
dict_list = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Alice', 'age': 30}
]

print(remove_duplicates_dicts_list_comprehension(dict_list))  # Output: [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

# Method 4: Using pandas Library

'''If you are working with large data or prefer using pandas, 
you can convert the list of dictionaries to a DataFrame and then drop duplicates.'''

import pandas as pd

def remove_duplicates_dicts_pandas(lst):
    df = pd.DataFrame(lst)
    df.drop_duplicates(inplace=True)
    return df.to_dict(orient='records')

# Example usage
dict_list = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Alice', 'age': 30}
]

print(remove_duplicates_dicts_pandas(dict_list))  # Output: [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

# Method 5: Using itertools.groupby

from itertools import groupby
from operator import itemgetter

def remove_duplicates_dicts_groupby(lst):
    sorted_lst = sorted(lst, key=itemgetter('name', 'age'))
    return [next(g) for k, g in groupby(sorted_lst, key=itemgetter('name', 'age'))]

# Example usage
dict_list = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Alice', 'age': 30}
]

print(remove_duplicates_dicts_groupby(dict_list))  # Output: [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

# Method 6: Using JSON Serialization

import json

def remove_duplicates_dicts_json(lst):
    seen = set()
    result = []
    for d in lst:
        json_str = json.dumps(d, sort_keys=True)
        if json_str not in seen:
            seen.add(json_str)
            result.append(d)
    return result

# Example usage
dict_list = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Alice', 'age': 30},
]

print(remove_duplicates_dicts_json(dict_list))  # Output: [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
