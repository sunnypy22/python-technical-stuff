### 1. Using the `update()` Method

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1) 

### 2. Using the `**` Operator

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict) 

### 3. Using Dictionary Comprehension

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {k: v for d in (dict1, dict2) for k, v in d.items()}
print(merged_dict) 

### 4. Using the `|` Operator (Python 3.9+)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1 | dict2
print(merged_dict)  

### 5. Using `collections.ChainMap` (For Read-Only Merging)


from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict(ChainMap(dict2, dict1))
print(merged_dict) 

### 6. Using `dict()` Constructor with `items()` Method

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict(dict1.items() | dict2.items())
print(merged_dict) 

### 7. Using `reduce()` from `functools`

from functools import reduce

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = reduce(lambda d1, d2: {**d1, **d2}, [dict1, dict2])
print(merged_dict) 
### 8. Using a For Loop


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1.copy()
for k, v in dict2.items():
    merged_dict[k] = v
print(merged_dict) 

### 9. Using `copy()` Method

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1.copy()
merged_dict.update(dict2)
print(merged_dict) 

### 10. Using `itertools.chain` (For Read-Only Merging)

import itertools

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict(itertools.chain(dict1.items(), dict2.items()))
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}
