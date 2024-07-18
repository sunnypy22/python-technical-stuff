### 1. Using a `set`

'''This method does not preserve the order of elements.'''


def remove_duplicates_set(lst):
    return list(set(lst))

print(remove_duplicates_set([1, 2, 2, 3, 4, 4, 5])) 

### 2. Using a `set` and List Comprehension (Order Preserved)

def remove_duplicates_set_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

print(remove_duplicates_set_order([1, 2, 2, 3, 4, 4, 5]))  

### 3. Using a `dict` (Python 3.7+ maintains insertion order)

def remove_duplicates_dict(lst):
    return list(dict.fromkeys(lst))

print(remove_duplicates_dict([1, 2, 2, 3, 4, 4, 5])) 

### 4. Using a For Loop (Order Preserved)

def remove_duplicates_loop(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates_loop([1, 2, 2, 3, 4, 4, 5])) 

### 5. Using `collections.OrderedDict` (Order Preserved)

from collections import OrderedDict

def remove_duplicates_ordereddict(lst):
    return list(OrderedDict.fromkeys(lst))

print(remove_duplicates_ordereddict([1, 2, 2, 3, 4, 4, 5])) 

### 6. Using Pandas (Order Preserved)

import pandas as pd

def remove_duplicates_pandas(lst):
    return pd.Series(lst).drop_duplicates().tolist()

print(remove_duplicates_pandas([1, 2, 2, 3, 4, 4, 5])) 

### 7. Using Numpy (Order Not Preserved)

import numpy as np

def remove_duplicates_numpy(lst):
    return np.unique(lst).tolist()

print(remove_duplicates_numpy([1, 2, 2, 3, 4, 4, 5])) 

### 8. Using List Comprehension with Conditional Logic (Order Preserved)

def remove_duplicates_conditional(lst):
    return [x for i, x in enumerate(lst) if x not in lst[:i]]

print(remove_duplicates_conditional([1, 2, 2, 3, 4, 4, 5])) 

### 9. Using `itertools.groupby` (Order Preserved)
'''This method requires the list to be sorted first.'''


from itertools import groupby

def remove_duplicates_groupby(lst):
    return [key for key, _ in groupby(sorted(lst))]

print(remove_duplicates_groupby([1, 2, 2, 3, 4, 4, 5]))