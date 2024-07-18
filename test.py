'''reverse list'''

# a = [2,2,3,4,5,5,6,6,7]

# def reverse_list(a):
#     # result = a[::-1]   # Using negative index
#     # result = list(reversed(a))  # Using reversed keyword
#     result = []    # Using insert index place and value
#     for i in a:
#         result.insert(0,i)
#     return result

# print("Reverse List : ",reverse_list(a))

'''check palindrome string'''

# input = "A man, a plan, a canal, Panama"

# def is_palindrome(input):
#     cleaned = ''.join(char.lower() for char in input if char.isalnum())
#     return cleaned == cleaned[::-1]

# print("Is palindrome : ",is_palindrome(input))

'''factorial number'''

# number = 5 

# def factorial_number(number):
#     result = 1
#     if number >= 1 and int(number):
#         for i in range(1,number+1):
#             result *= i
#         return result
#     else:
#         return "Please Insert the relevant number"
    

# print(factorial_number(number))

'''Remove Duplicate from list'''

# input = [1,1,1,2,3,4,5]

# def remove_duplicate(input):
#     # result = list(set(input)) # Using set
#     result = []
#     for i in input:
#         if i not in result:
#             result.append(i)
#     return result

# print(remove_duplicate(input))

'''Count the specific vowels'''

# vowels = 'aeiou'
# input = 'hello there'

# def count_vowels(input):
#     vowel_count = {v:0 for v in vowels}
    
#     for char in input.lower():
#         if char in vowels:
#             vowel_count[char] += 1
        
#     return {v: vowel_count[v] for v in vowel_count if vowel_count[v] > 0}

# print("Count Vowels",count_vowels(input))



'''compute the Nth fibonacci number'''

# number = 9

# def fibonacci_number(number):
#     value = []
#     a,b = 0,1
#     for i in range(number+1):
#         value.append(a)
#         a,b = b,a+b
    
#     return value[-1]

# print("fibonacci_number:",fibonacci_number(number))

'''generate fibonacci series'''

# number = 10

# def generate_fibonacci(number):
#     value = []
#     a,b = 0,1
#     for i in range(number+1):
#         value.append(a)
#         a,b = b,a+b
    
#     return value
# print(generate_fibonacci(number))

'''Combine list in single string'''

# s =["Hello", "world", "this", "is", "a", "test"]

# def string(s):
#     return ' '.join(s)

# print(string(s))

'''Split string into a list'''

# def split_string_into_words(input_string):
#     words_list = input_string.split()
#     return words_list

# sentence = "Hello world this is a test"
# words = split_string_into_words(sentence)
# print(words)

'''Most Frequent Element and frequency of element'''

# numbers = [1, 2, 3, 1, 2, 2, 3, 1, 2, 2, 2]


# def most_frequent_element(numbers):
#     value = {v:0 for v in numbers}
#     for element in numbers:
#         if element in value:
#             value[element] += 1
#     print("Frequency of Element : ",value)
#     max_value = max(value,key=value.get) 
    
#     return f'{max_value}:{value[max_value]}'  

# print("most frequent element :" ,most_frequent_element(numbers))

'''remove all occurrences of a specific element from a list'''

# input_list = [1, 2, 3, 4, 2, 2, 5]
# element_to_remove = 2

# def remove_from_list(input,element):
#     while element in input:
#         input_list.remove(element)
#     return input

# print("Removed Element from list : ",remove_from_list(input_list,element_to_remove))

'''flatten_recursive'''

# nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, [9]]]

# def flatten_recursive(nested_list):
#     flattened_list = []
#     for i in nested_list:
#         if isinstance(i, list):
#             flattened_list.extend(flatten_recursive(i))
#         else:
#             flattened_list.append(i)
#     return flattened_list

# result = flatten_recursive(nested_list)
# print("Flattened list:", result)

'''Count the occurences of each word'''

# input_string = "hello world hello python world"

# def count_occurence_word(input):
#     new_list = input.split()
#     result = {v:0 for v in new_list}
#     for i in new_list:
#         if i in result:
#             result[i] += 1
#     return result

# print(count_occurence_word(input_string))


'''check if string start with specific prefix'''

# string = "Hello, world!"
# prefix = "Hello"

# def starts_with_using_slicing(string, prefix):
#     return string[:len(prefix)] == prefix

# print(starts_with_using_slicing(string, prefix))