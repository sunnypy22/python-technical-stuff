#1. Using the reverse() Method
'''This method reverses the list in place'''

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

#2. Using List Slicing
'''This creates a new list that is the reverse of the original list.'''

my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)

#3. Using the reversed() Function
'''This returns an iterator that accesses the given sequence in the reverse order.'''

my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(reversed_list)

#4. Using a for Loop
'''This creates a new list by appending elements in reverse order.'''

my_list = [1, 2, 3, 4, 5]
reversed_list = []
for item in my_list:
    reversed_list.insert(0, item)
print(reversed_list)

#5. Using List Comprehension
'''This is another way to create a new list using list comprehension.'''

my_list = [1, 2, 3, 4, 5]
reversed_list = [my_list[i] for i in range(len(my_list)-1, -1, -1)]
print(reversed_list)

#6. Using while Loop
my_list = [1, 2, 3, 4, 5]
reversed_list = []
i = len(my_list) - 1
while i >= 0:
    reversed_list.append(my_list[i])
    i -= 1
print(reversed_list)

#7. Using reduce() from functools
'''This uses reduce() to accumulate the reversed list.'''

from functools import reduce

my_list = [1, 2, 3, 4, 5]
reversed_list = reduce(lambda acc, x: [x] + acc, my_list, [])
print(reversed_list)

# 8. Using Deque from collections
'''Deque has an appendleft() method which can be used to reverse a list efficiently.'''

from collections import deque

my_list = [1, 2, 3, 4, 5]
d = deque()
for item in my_list:
    d.appendleft(item)
reversed_list = list(d)
print(reversed_list)
