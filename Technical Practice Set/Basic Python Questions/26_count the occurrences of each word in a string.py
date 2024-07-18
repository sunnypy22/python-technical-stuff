# Using Python Standard Libraries

def count_words(input_string):
    # Splitting the input string into words
    words = input_string.split()

    # Initializing an empty dictionary to store word counts
    word_count = {}

    # Counting occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Example usage
input_string = "hello world hello python world"
result = count_words(input_string)
print("Word counts:", result)
